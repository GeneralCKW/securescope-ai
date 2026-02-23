import uuid
from sqlalchemy import Column, ForeignKey, Float, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base

class Response(Base):
    __tablename__ = "responses"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    assessment_id = Column(UUID(as_uuid=True), ForeignKey("assessments.id"))
    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id"))
    answer = Column(Boolean) # e.g., 1-5 scale
    calculated_risk_value = Column(Float)
    
    assessment = relationship("Assessment", back_populates="responses")
    question = relationship("Question", back_populates="responses")