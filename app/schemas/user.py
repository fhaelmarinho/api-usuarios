from pydantic import BaseModel
from uuid import UUID

class UserCreate(BaseModel):
    name: str
    email: str
    phone: str
    country: str
    state: str
    city: str

class UserResponse(BaseModel):
    id: UUID
    name: str
    email: str
    phone: str
    country: str
    state: str
    city: str