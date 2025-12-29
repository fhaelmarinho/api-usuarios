from fastapi import FastAPI
from app.schemas.user import UserCreate
from app.database import SessionLocal
from app.models.user import User

app = FastAPI()

@app.post("/users")
def create_user(user: UserCreate):
    db = SessionLocal()

    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    db.close()
    return db_user
