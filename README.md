# Affiliate Link Tracking System

A FastAPI-based system for tracking affiliate links, clicks, and revenue.

## Current Features

- Create and manage affiliate links
- Track clicks with automatic redirection
- Track revenue per link
- View link statistics (clicks and revenue)
- Simple WSGI deployment on shared hosting

## API Endpoints

### Health Check
- `GET /health` - Check system status

### Link Management
- `GET /api/links` - List all links
- `POST /api/links` - Create a new link
  ```json
  {
    "url": "https://example.com",
    "name": "Example Link"
  }
  ```

### Click Tracking
- `GET /click/{link_id}` - Track click and redirect to target URL

### Revenue Tracking
- `POST /api/links/{link_id}/revenue` - Update link revenue
  ```json
  {
    "amount": 10.50
  }
  ```

## Project Structure

```
.backend/
├── main.py          - Main application and WSGI entry point
├── models.py        - Database models
├── database.py      - Database configuration
├── requirements.txt - Python dependencies
└── test_api.py     - API test script
```

## Roadmap

### Security
- [ ] Add authentication for admin endpoints
- [ ] Add rate limiting for click tracking
- [ ] Add IP tracking for click validation
- [ ] Implement API key system

### Features
- [ ] Add link categories/tags
- [ ] Add date range filtering for statistics
- [ ] Add revenue goals and notifications
- [ ] Add bulk link creation/update
- [ ] Add link expiration dates
- [ ] Add custom redirect paths

### Analytics
- [ ] Add detailed click analytics (referrer, device, etc.)
- [ ] Add revenue charts and reports
- [ ] Add conversion tracking
- [ ] Add A/B testing capabilities

### Administration
- [ ] Add user management system
- [ ] Add role-based access control
- [ ] Add audit logging
- [ ] Add backup/restore functionality

### Frontend
- [ ] Create admin dashboard
- [ ] Add real-time statistics
- [ ] Create mobile-friendly interface
- [ ] Add link management UI

### Integration
- [ ] Add webhook support for events
- [ ] Add email notifications
- [ ] Add export/import functionality
- [ ] Add API documentation (Swagger/OpenAPI)

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure environment variables:
   ```
   DATABASE_URL=sqlite:///./test.db
   ```

3. Run the application:
   - For development: Use uvicorn
   - For production: Use the WSGI setup

## Testing

Run the test script to verify functionality:
```bash
python test_api.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT License
