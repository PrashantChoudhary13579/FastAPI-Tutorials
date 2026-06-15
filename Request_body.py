from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    item_id :int
    name: str
    description:str|None = None
    price: float
    tax: float|None = None

app = FastAPI()

# Here we have post - used to create item
@app.post("/item/")
async def create_item(item : Item):
    item_dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax":price_with_tax})
    
    return item_dict

