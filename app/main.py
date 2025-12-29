from fastapi import FastAPI
from app.schemas.user import UserCreate

app = FastAPI()

@app.post("/UserCreate")
def create_user(user: UserCreate):
    return{
        "message": "User created","user": user
        }
    
    