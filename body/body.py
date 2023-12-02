from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    name: str
    city: str
    age: int

@router.post("/create_user")
async def create_user(user: User):
    return user