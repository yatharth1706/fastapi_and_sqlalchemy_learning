from fastapi import APIRouter
from classes.user import User

router = APIRouter()

@router.put("/user/{user_id}")
def update_user(user_id: str, user: User):
    return {
        "message": "User updated successfully",
        "user": user,
        "user_id": user_id
    }
