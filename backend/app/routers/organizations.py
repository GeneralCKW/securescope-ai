from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.organization import Organization
from app.schemas.organization import OrganizationCreate, OrganizationResponse
from app.models.user import User
from app.auth import get_current_user
import uuid

router = APIRouter(prefix="/organizations", tags=["Organizations"])

@router.post("/", response_model=OrganizationResponse)
def create_org(
    org: OrganizationCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)):
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
def get_orgs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Organization).all()