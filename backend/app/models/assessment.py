import uuid
from sqlalchemy import Column, String, ForeignKey, Float, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Assessment(Base):
    __tablename__ = "assessments"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"))
    status = Column(String, default="In Progress")
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    risk_score = Column(Float, default=0)
    risk_level = Column(String, default="Low")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    organization = relationship("Organization", back_populates="assessments")
    responses = relationship("Response", back_populates="assessment")