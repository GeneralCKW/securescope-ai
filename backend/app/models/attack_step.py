import uuid
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base

class AttackStep(Base):
    __tablename__ = "attack_steps"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    attack_path_id = Column(UUID(as_uuid=True), ForeignKey("attack_paths.id"))
    step_order = Column(Integer)
    technique = Column(String)
    description = Column(String)