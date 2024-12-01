from fastapi import FastAPI, HTTPException
from typing import List

from database import menu, orders, reviews
from models import MenuItem, Order, Review


app = FastAPI(
    docs_url="/docs", 
    redoc_url="/redoc", 
    openapi_url="/openapi.json"  
)


# Endpoints
@app.get("/")
def read_root():
    return {"message": "Welcome to the Cafe API!"}


@app.get("/menu", response_model=List[MenuItem])
def get_menu():
    return menu

@app.post("/menu")
def add_menu_item(item: MenuItem):
    if any(i.id == item.id for i in menu):
        raise HTTPException(status_code=400, detail="Item with this ID already exists.")
    menu.append(item)
    return {"message": "Menu item added successfully!"}

@app.get("/orders", response_model=List[Order])
def get_orders():
    return orders

@app.post("/order")
def place_order(order: Order):
    total_price = sum(menu_item.price for menu_item in menu if menu_item.id in order.items)
    order.total = total_price
    orders.append(order)
    return {"message": f"Order placed successfully! Total: ${total_price}"}

@app.post("/reviews")
def add_review(review: Review):
    if not any(item.id == review.item_id for item in menu):
        raise HTTPException(status_code=404, detail="Menu item not found.")
    reviews.append(review)
    return {"message": "Review added successfully!"}

@app.get("/reviews", response_model=List[Review])
def get_reviews():
    return reviews
