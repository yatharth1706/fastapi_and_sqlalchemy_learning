from fastapi import APIRouter, Cookie
from typing import Annotated

router = APIRouter()

@router.get("/get_cookie")
def get_cookie(token: Annotated[str, Cookie()]):
    return {
        "token": token
    }