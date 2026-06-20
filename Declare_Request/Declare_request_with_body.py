from typing import Annotated
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name:str
    description:str|None = None
    price:float
    tax: float|None = None

@app.put("/item/{item_id}")
async def update_item(
    item_id:int,
    item:Annotated[
        Item,
        Body(
            examples=[
                {
                    "name":"Money",
                    "descrption":"Not everyone can afford it.",
                    "price":999999,
                    "tax":30,
                }
            ],
        ),
    ],
):
    result = {"item_id":item_id, "item":item}
    return result

    # You can also do it with multiple examples