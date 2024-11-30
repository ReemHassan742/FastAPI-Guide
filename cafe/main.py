from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List 
from database import menu, orders, reviwes


app = FastAPI()

class MenuItems(BaseModel):
    id: int
    name:str
    price: float
    desqription: str
    
class Order(BaseModel):
    id: int
    items: List[int]
    total: float = 0.0
    
class Review(BaseModel):
    item_id: int
    review: str
    rating: int #From 1 to 5    

#Endpoints

@app.get("/menu", response_model=List[MenuItems])
def get_menu():
    return menu 

@app.post("/menu")
def add_menu_item(item: MenuItems):
    if any(i.id == item.id for i in menu):
        raise HTTPException(status_code=400, detail="Item with this ID already exists.")
    menu.append(item)
    return {"message":"Menu item added successfully!"}

@app.get("/orders", response_model=List[Order])
def get_orders():
    return orders

@app.post("/order")
def place_order(order: Order):
    total_price = sum(menu_item.price for menu_item in menu if menu_item.id in order.items)
    order.total = total_price
    orders.append(order)
    return {"message": f"order placed successfully! Total: ${total_price}"}

@add.post("/reviews")
def add_reveiw(review: Review):
    if not any(item.id == review.item_id for item in menu):
        raise HTTPException(status_code=404, detail="Menu item not found.")
    reviwes.append(review)
    return {"massage":"Review added successfully!"}

@app.get("/reviews", response_model=List[Review])
def get_reviews():
    return reviwes
