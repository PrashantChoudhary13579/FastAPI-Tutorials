from fastapi import Body, FastAPI
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str|None = None
    price: float
    tax : float |None = None

class User(BaseModel):
    username: str
    fullname: str |None = None

@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id:int, 
    item:Item, 
    user:User, 
    importance:Annotated[int, Body(gt=0)],
    q: str|None = None
):
    result = {
        "item_id":item_id,
        "item":item,
        "user":user,
        "importance":importance
    }
    if q:
        result.update({"q":q})
    return result