from fastapi import FastAPI
import logging
import json
from database import engine, SessionLocal
import models
from sqlalchemy.orm import Session

# Create tables
models.Base.metadata.create_all(bind=engine)

# Configure logging
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create FastAPI instance
fastapi_app = FastAPI()

def get_links_from_db():
    """Helper function to get links from database"""
    try:
        db = SessionLocal()
        links = db.query(models.Link).all()
        return [
            {
                "id": link.id,
                "url": link.url,
                "name": link.name,
                "clicks": link.clicks,
                "revenue": float(link.revenue)
            } for link in links
        ]
    except Exception as e:
        logger.error(f"Database error: {str(e)}")
        return []
    finally:
        db.close()

def create_link_in_db(url: str, name: str):
    """Helper function to create a new link"""
    try:
        db = SessionLocal()
        link = models.Link(url=url, name=name)
        db.add(link)
        db.commit()
        db.refresh(link)
        return {
            "id": link.id,
            "url": link.url,
            "name": link.name,
            "clicks": link.clicks,
            "revenue": float(link.revenue)
        }
    except Exception as e:
        logger.error(f"Database error creating link: {str(e)}")
        db.rollback()
        raise
    finally:
        db.close()

def track_click(link_id: int):
    """Helper function to track a click"""
    try:
        db = SessionLocal()
        link = db.query(models.Link).filter(models.Link.id == link_id).first()
        if link:
            link.clicks += 1
            db.commit()
            return link.url
        return None
    except Exception as e:
        logger.error(f"Database error tracking click: {str(e)}")
        db.rollback()
        raise
    finally:
        db.close()

def update_revenue(link_id: int, amount: float):
    """Helper function to update link revenue"""
    try:
        db = SessionLocal()
        link = db.query(models.Link).filter(models.Link.id == link_id).first()
        if link:
            link.revenue += amount
            db.commit()
            db.refresh(link)
            return {
                "id": link.id,
                "url": link.url,
                "name": link.name,
                "clicks": link.clicks,
                "revenue": float(link.revenue)
            }
        return None
    except Exception as e:
        logger.error(f"Database error updating revenue: {str(e)}")
        db.rollback()
        raise
    finally:
        db.close()

def read_post_data(environ):
    """Helper function to read POST data"""
    try:
        content_length = int(environ.get('CONTENT_LENGTH', 0))
        body = environ['wsgi.input'].read(content_length).decode('utf-8')
        return json.loads(body)
    except Exception as e:
        logger.error(f"Error reading POST data: {str(e)}")
        raise

def app(environ, start_response):
    """WSGI application that forwards requests to FastAPI"""
    path = environ.get('PATH_INFO', '').rstrip('/')
    method = environ.get('REQUEST_METHOD', 'GET')
    logger.debug(f"{method} request received for path: {path}")
    
    # Strip any trailing slashes and ensure path starts with /
    if not path:
        path = '/health'
    elif not path.startswith('/'):
        path = '/' + path
        
    logger.debug(f"Normalized path: {path}")
    
    try:
        if path == '/health':
            response_data = {"status": "healthy", "version": "1.0.0"}
            status = '200 OK'
            response_headers = [('Content-type', 'application/json')]
        elif path.startswith('/click/'):
            try:
                link_id = int(path.split('/')[-1])
                target_url = track_click(link_id)
                if target_url:
                    status = '302 Found'
                    response_headers = [('Location', target_url)]
                    response_data = {}
                else:
                    status = '404 Not Found'
                    response_headers = [('Content-type', 'application/json')]
                    response_data = {"error": "Link not found"}
            except ValueError:
                status = '400 Bad Request'
                response_headers = [('Content-type', 'application/json')]
                response_data = {"error": "Invalid link ID"}
        elif path.startswith('/api/links/'):
            if method == 'POST' and path.endswith('/revenue'):
                try:
                    link_id = int(path.split('/')[-2])
                    post_data = read_post_data(environ)
                    amount = float(post_data.get('amount', 0))
                    
                    if amount <= 0:
                        status = '400 Bad Request'
                        response_data = {"error": "Amount must be positive"}
                    else:
                        link = update_revenue(link_id, amount)
                        if link:
                            status = '200 OK'
                            response_data = {"link": link}
                        else:
                            status = '404 Not Found'
                            response_data = {"error": "Link not found"}
                except (ValueError, TypeError):
                    status = '400 Bad Request'
                    response_data = {"error": "Invalid link ID or amount"}
            else:
                status = '404 Not Found'
                response_data = {"error": "Invalid endpoint"}
            response_headers = [('Content-type', 'application/json')]
        elif path == '/api/links':
            if method == 'GET':
                links = get_links_from_db()
                response_data = {"links": links}
                status = '200 OK'
            elif method == 'POST':
                post_data = read_post_data(environ)
                url = post_data.get('url')
                name = post_data.get('name')
                
                if not url or not name:
                    status = '400 Bad Request'
                    response_data = {"error": "URL and name are required"}
                else:
                    link = create_link_in_db(url=url, name=name)
                    response_data = {"link": link}
                    status = '201 Created'
            else:
                status = '405 Method Not Allowed'
                response_data = {"error": "Method not allowed"}
            response_headers = [('Content-type', 'application/json')]
        else:
            status = '404 Not Found'
            response_data = {"error": "Not Found", "path": path}
            response_headers = [('Content-type', 'application/json')]
            
        start_response(status, response_headers)
        if response_headers[0][0] == 'Location':
            return [b'']
        return [json.dumps(response_data).encode('utf-8')]
        
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        status = '500 Internal Server Error'
        response_headers = [('Content-type', 'application/json')]
        start_response(status, response_headers)
        return [json.dumps({"error": str(e)}).encode('utf-8')]
