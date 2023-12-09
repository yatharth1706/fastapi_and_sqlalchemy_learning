from fastapi import APIRouter, Query
from typing import Annotated

router = APIRouter()

# Here we are validating if query is given its max length should be 50 and min length should be 3
@router.get("/items/")
def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50)] = None):
    results = {
        "items": [{"item_id": "12312"}, {"item_id": "12414"}]
    }
    
    if(q):
        results.update({q: q})

    return results
    