from pydantic import BaseModel
from pydantic import Field
from uuid import UUID, uuid4

class UserCreate(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    email: str
    phone: str
    country: str
    state: str
    city: str
    
    
