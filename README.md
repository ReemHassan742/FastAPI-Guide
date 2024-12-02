# FastAPI-Guide
Welcome to the FastAPI Guide! This repository serves as an in-depth exploration of FastAPI, complete with examples, explanations, and a practical project: a Cafe Management API.

What is FastAPI?
FastAPI is a modern, fast (high-performance), and easy-to-use Python web framework designed to build APIs with Python 3.7+ based on standard Python type hints. It's particularly appreciated for its:

Speed: Comparable to Node.js and Go.
Ease of Use: Interactive docs and developer-friendly.
Type Safety: Leverages Python type hints for request validation and response serialization.
Getting Started with FastAPI
Installation
Install FastAPI and Uvicorn (ASGI server):

bash
Copy code
pip install fastapi uvicorn
Running a FastAPI Application
Create a file main.py with a simple FastAPI app:

python
Copy code
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
Start the server:

bash
Copy code
uvicorn main:app --reload
Interactive Documentation
Visit /docs (Swagger UI) or /redoc for automatically generated interactive documentation.

Cafe Management Project
Overview
This project demonstrates a practical implementation of FastAPI for managing a cafe's menu, orders, and customer reviews. It includes the following features:

Menu Management: Add, update, and view menu items.
Order Management: Place and view customer orders.
Review Management: Add and view customer reviews for menu items.
Project Structure
bash
Copy code
FastAPI-Guide/
│
├── main.py           # Main FastAPI application
├── models.py         # Data models for the project
├── database.py       # Simulated in-memory database
├── requirements.txt  # Project dependencies
└── README.md         # This file
Examples from the Project
1. Add a Menu Item
Request:
POST /menu
Body:

json
Copy code
{
    "id": 3,
    "name": "Latte",
    "price": 4.5,
    "description": "Rich espresso with steamed milk."
}
Response:

json
Copy code
{
    "message": "Menu item added successfully!"
}
2. Place an Order
Request:
POST /order
Body:

json
Copy code
{
    "id": 1,
    "items": [1, 2]
}
Response:

json
Copy code
{
    "message": "Order placed successfully! Total: $5.5"
}
3. Add a Review
Request:
POST /reviews
Body:

json
Copy code
{
    "item_id": 1,
    "review": "Amazing espresso, would recommend!",
    "rating": 5
}
Response:

json
Copy code
{
    "message": "Review added successfully!"
}


Here are some helpful resources to learn more about FastAPI:

Official Documentation (https://fastapi.tiangolo.com/)
Uvicorn Documentation (https://www.uvicorn.org/)
How to Use FastAPI (https://youtu.be/SORiTsvnU28?si=CeduJuFkJ5R-UuWs)
FastAPI playlist (https://www.youtube.com/watch?v=nCrX79LqDT8&list=PLqAmigZvYxIL9dnYeZEhMoHcoP4zop8-p)



Medium Article
The full explanation of this project and its implementation can be found on my Medium blog:
FastAPI Guide: Building a Cafe Management API (link to be updated)
