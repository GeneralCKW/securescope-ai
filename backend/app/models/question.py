"""
Question model.

Represents a security control question used in risk assessments.
Each question contains a risk weight that contributes ot the overall
risk score if the control is not implemented.
"""

import uuid
from sqlalchemy import Column, String, Float
from app.models.assessment import Assessment
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base

class Question(Base):
    """
    Security assessment question.
    
    Attributes:
        id (UUID): Unique identifier for the question
        question_text (str): The question text presented to the user
        weight (int): Risk score weight if control fails
    """
    
    __tablename__ = "questions"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category = Column(String) 
    question_text = Column(String, nullable=False)
    weight = Column(Float, default=1.0)
    risk_factor_tag = Column(String)
    
    responses = relationship("Response", back_populates="question")