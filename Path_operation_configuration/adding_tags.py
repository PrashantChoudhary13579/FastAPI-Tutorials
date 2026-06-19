from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    description:str |None = None
    price: float 
    tax: float |None = None
    tags: set[str] = set()

@app.post("/items/", tags=["items"],summary="Create an item",response_description= 'The item is created',)
async def create_item( item: Item)-> Item:
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item

# Works as the description..

@app.get('/items/', tags=['items'], description="Reading the name and the price of the item.. " , summary='Detail of the product', deprecated=True)
# Deprecated = true will mark it as deleted. 
async def read_item():
    return [{"name":"Foo", "price":42}]

# Also description, but this one has higher priority over the previous one.. so called inline.


# tags separate out the users... think tags as class and methods as function in a class

@app.get("/users/", tags=['users'])
async def read_users():
    return [{"username": "prashant"}]