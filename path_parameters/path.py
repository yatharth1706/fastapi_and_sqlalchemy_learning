from fastapi import APIRouter

router = APIRouter()

@router.get("/persons/{person_id}")
async def get_persons(person_id: str):
    return {"person_id": person_id}