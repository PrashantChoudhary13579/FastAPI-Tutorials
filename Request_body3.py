# This include = Request body + Path + Query Parameter 
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str|None = None
    price : float
    tax: float |None = None

# Here we have put - used for updation
@app.put("/items/{item_id}")
async def update_item(
    item_id : int, item:Item, q: str |None= None
):
    result =  {"item_id":item_id , **item.model_dump()}
    if q:
        result.update({"q" : q})
    return result

