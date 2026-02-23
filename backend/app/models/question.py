import uuid
from sqlalchemy import Column, String, Float
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base

class Question(Base):
    __tablename_ = "questions"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category = Column(String) # e.g., "auth", "network", "compliance"
    question_text = Column(String, nullable=False)
    weight = Column(Float, default=1.0)
    risk_factor_tag = Column(String)
    # Additional fields can be added as needed, such as references to specific controls or standards.