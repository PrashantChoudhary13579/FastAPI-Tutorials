from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url : HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: str |None = None
    price: float
    tax: float|None = None
    tags: set[str] =set()
    image: list[Image] |None = None


@app.put("/item/{item_id}")
async def update_item(
    item_id:int, item: Item
):
    result = {"item_id":item_id, "item": item}
    return result