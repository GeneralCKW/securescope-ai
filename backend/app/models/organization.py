import uuid
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.assessment import Assessment
from app.database import Base

class Organization(Base):
    __tablename__ = "organizations"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, nullable=False)
    industry = Column(String, default="Healthcare")
    size = Column(String, nullable=True)
    assessments = relationship("Assessment", back_populates="organization")