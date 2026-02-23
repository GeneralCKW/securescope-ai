from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.organization import Organization
from app.schemas.organization import OrganizationCreate, OrganizationResponse

import uuid

router = APIRouter(prefix="/organizations", tags=["Organizations"])

@router.post("/", response_model=OrganizationResponse)
def create_org(org: OrganizationCreate, db: Session = Depends(get_db)):
    db_org = Organization(
        id=uuid.uuid4(),
        name=org.name,
        industry=org.industry,
        size=org.size
    )
    db.add(db_org)
    db.commit()
    db.refresh(db_org)
    return db_org

@router.get("/", response_model=list[OrganizationResponse])
def get_orgs(db: Session = Depends(get_db)):
    return db.query(Orgnization).all()