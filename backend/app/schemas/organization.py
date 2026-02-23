from pydantic import BaseModel
from uuid import UUID

class OrganizationCreate(BaseModel):
    name: str
    industry: str
    size: str | None = None
    
class OrganizationResponse(BaseModel):
    id: UUID
    name: str
    industry: str
    size: str | None = None
    
    class Config:
        from_attributes = True