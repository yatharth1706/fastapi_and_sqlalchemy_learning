from fastapi import APIRouter
from enum import Enum

router = APIRouter()

class EnumValue(str, Enum):
    spiderman= "spiderman"
    batman = "batman"
    superman = "superman"
    ironman = "ironman"
    doctorStrange = "doctorStrange"

@router.get("/enum/{enum_value}")
def get_enum(enum_value: EnumValue):
    return {"enum": enum_value}