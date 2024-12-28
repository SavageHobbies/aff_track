from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import Link, Application, Earning, Report

router = APIRouter()

@router.delete("/dashboard/clear")
async def clear_dashboard(db: Session = Depends(get_db)):
    """Clear all dashboard data"""
    try:
        # Clear metrics and statistics
        db.execute("DELETE FROM metrics")
        db.execute("DELETE FROM statistics")
        db.commit()
        return {"message": "Dashboard data cleared successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/applications/clear")
async def clear_applications(db: Session = Depends(get_db)):
    """Clear all applications"""
    try:
        db.query(Application).delete()
        db.commit()
        return {"message": "All applications cleared successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/applications/{application_id}")
async def delete_application(application_id: int, db: Session = Depends(get_db)):
    """Delete a single application"""
    application = db.query(Application).filter(Application.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    
    db.delete(application)
    db.commit()
    return {"message": "Application deleted successfully"}

@router.delete("/earnings/clear")
async def clear_earnings(db: Session = Depends(get_db)):
    """Clear all earnings data"""
    try:
        db.query(Earning).delete()
        db.commit()
        return {"message": "All earnings cleared successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/earnings/{earning_id}")
async def delete_earning(earning_id: int, db: Session = Depends(get_db)):
    """Delete a single earning record"""
    earning = db.query(Earning).filter(Earning.id == earning_id).first()
    if not earning:
        raise HTTPException(status_code=404, detail="Earning record not found")
    
    db.delete(earning)
    db.commit()
    return {"message": "Earning record deleted successfully"}

@router.delete("/reports/clear")
async def clear_reports(db: Session = Depends(get_db)):
    """Clear all reports"""
    try:
        db.query(Report).delete()
        db.commit()
        return {"message": "All reports cleared successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/reports/{report_id}")
async def delete_report(report_id: int, db: Session = Depends(get_db)):
    """Delete a single report"""
    report = db.query(Report).filter(Report.id == report_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    
    db.delete(report)
    db.commit()
    return {"message": "Report deleted successfully"}
