from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Item(BaseModel):
    name: str
    description : str |None = None
    price: float
    tax: float|None = None

items = {
    "foo":{
        "name":"Foo",
        "price":100,
    },
    "bar":{
        "name":"Bar",
        "description":"The bar fighters",
        "price":62,
        "tax":20.2
    },
    "baz":{
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}

@app.get("/item/{item_id}/name", response_model=Item, response_model_include=["name","description"])
async def read_item(item_id:str):
    return items[item_id]

@app.get("/item/{item_id}/public", response_model= Item, response_model_exclude=["tax"])
async def read_item_public_data(item_id:str):
    return items[item_id]
