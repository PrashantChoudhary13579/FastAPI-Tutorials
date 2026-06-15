# This include = Request body + Path parameters
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
async def update_item(item_id : int, item:Item):
    return {"item_id":item_id , **item.model_dump()}

