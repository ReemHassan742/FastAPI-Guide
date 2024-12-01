from pydantic import BaseModel
from typing import List


class MenuItem(BaseModel):
    id: int
    name: str
    price: float
    description: str


class Order(BaseModel):
    id: int
    items: List[int]  
    total: float = 0.0


class Review(BaseModel):
    item_id: int 
    review: str
    rating: int  # Rating out of 5
