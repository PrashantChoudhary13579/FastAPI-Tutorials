from fastapi import FastAPI , Body
from pydantic import BaseModel, Field
from typing import Annotated

router = FastAPI()

class Item(BaseModel):
    name : str
    description: str | None = Field(
        default = None, title="The description of the item", max_length=300
    )
    price: float = Field(
        gt = 0, description ="Description of the Price"
    )
    tax: float |None = None
    tags:list = [] # list[str] = [] - list of string
    # set[str] = set() - as a set of string // remove redundancy of data

@router.put("/items/{item_id}")
async def update_item(
    item_id: int, item: Annotated[Item,Body(embed=True)] 
):
    result = {"item_id":item_id, "item":item}
    return result

# Recap
# You can use Pydantic's Field to declare extra validations and metadata for model attributes.

# You can also use the extra keyword arguments to pass additional JSON Schema metadata