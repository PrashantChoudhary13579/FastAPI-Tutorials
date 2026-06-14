from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name :str
    price:float
    is_offer:Union[bool, None] = None


@app.get("")
async def read_root():
    return {"Hello":"How are you ?"}

@app.get("/items/{item_id}")
async def read_item(item_id:int, q: Union[bool,None] = None):
    return {"Item ID ": item_id, "q" : q }

@app.get("")

@app.put("/items/{item_id}")
async def update_item(item_id:int, item:Item):
    return {
        "Item ID: ": item_id,
        "Item Name: ": item.name,
        "Item Price" : item.price
    }