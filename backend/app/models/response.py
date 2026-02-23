import uuid
from sqlalchemy import Column, ForeignKey, Float, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base

class Response(Base):
    __tablename__ = "responses"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    assessment_id = Column(UUID(as_uuid=True), ForeignKey("asssessments.id"))
    question_id = Column(UUID(as_uuid=True), ForeignKey("questions.id"))
    answer = Column(Integer) # e.g., 1-5 scale
    calculated_risk_value = Column(Float)