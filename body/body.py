from fastapi import APIRouter, Body
from classes.user import User
from classes.item import Item
from typing import Annotated

router = APIRouter()

@router.post("/create_user")
async def create_user(user: User):
    return user


# In this example we are passing two different entities in body and also attaching one more param in body
# explicitly by using Body()
@router.put("/update_item_for_user/{user_id}")
async def update_item_for_user(user_id: str, item: Item, user: User, importance: Annotated[bool, Body()]):
    return {
        "user_id": user_id,
        "item": item,
        "user": user,
        "importance": importance
    }


# Next example is to explicitly allow fastapi to take the body parameter inside a key
@router.put("/embeded_body_item")
def update_item(item: Annotated[Item, Body(embed=True)]):
    return {
        "item": item
    }