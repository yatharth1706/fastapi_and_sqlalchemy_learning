from fastapi import APIRouter
from classes.user import User

router = APIRouter()

@router.post("/create_user")
async def create_user(user: User):
    return user