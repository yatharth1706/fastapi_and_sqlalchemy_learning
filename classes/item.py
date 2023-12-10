from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str
    price: int = Field(ge=10, description="The price must be greater than equal to 10")
    description: str