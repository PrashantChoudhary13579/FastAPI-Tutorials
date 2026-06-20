from fastapi import FastAPI, Body
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    description:str|None = None
    price: float
    tax: float |None = None

@app.put("/item/{item_id}")
async def update_item(
    *, 
    item_id:int,
    item: Annotated[
        Item, 
        Body(
            openapi_examples={
                "normal":{
                    "summary":"A normal talk about rich",
                    "description":"The only powerful person in this world is that which has most **money**",
                    "value":{
                        "name":"Money",
                        "description":"More the money, more powerful you are.",
                        "price": 999999,
                        "tax": 0,
                    },
                },
                "converted":{
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid":{
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                }
            },
        ),
    ],
):
    result ={"item_id": item_id, "item":item}
    return result

# external value can also be used..