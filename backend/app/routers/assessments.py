from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.assessment import Assessment
from app.services.risk_engine import calculate_risk_score
from uuid import UUID

router = APIRouter(prefix="/assessments", tags=["Assessments"])

@router.get("/{assessment_id}/risk")
def get_risk_score(assessment_id: UUID, db: Session = Depends(get_db)):
    assessment = db.query(Assessment).filter(Assessment.id == assessment_id).first()
    
    if not assessment:
        return {"error": "Assessment not foung"}
    
    risk_score = calculate_risk_score(assessment)
    
    return {
        "assessment_id": assessment_id,
        "risk_score": risk_score
    }