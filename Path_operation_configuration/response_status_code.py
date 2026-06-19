from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    description:str |None = None
    price: float
    tax: float|None = None
    tags: set[str] = set()
    # using set instead of list to remove the redundancy of data

@app.post("/item/{item_id}", status_code=status.HTTP_201_CREATED)
async def create_item(item:Item) -> Item:
    return item 

# That status code will be used in the response and will be added to the OpenAPI schema.