from typing import Annotated
from fastapi import APIRouter, Header

router = APIRouter()

@router.get("/get_header")
async def get_header(authorization: Annotated[str, Header()]):
    return {
        "authorization": authorization
    }