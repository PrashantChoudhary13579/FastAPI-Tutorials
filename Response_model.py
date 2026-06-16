from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any
app = FastAPI()

class Item(BaseModel):
    name: str
    description: str |None = None
    price: float
    tax: float |None = None
    x_tags: list[str] = []

@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Any:
    return item

@app.get("/items/", response_model= list[Item])
async def read_items() ->Any:
    return [
        {"name":"AK47 ","description":"Gun used by the terrorist", "price":30000},
        {"name":"Adidas", "price":1000, "tax": 100.5}
    ]