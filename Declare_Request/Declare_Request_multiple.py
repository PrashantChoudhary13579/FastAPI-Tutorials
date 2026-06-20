from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    description: str|None = None
    price: float
    tax: float|None = None
    model_config = {
        "json_schema_extra":{
            "examples": [         
                {
                    "name": "chalk",
                    "description": "Made up of CaCO3 (Calcium Carbonate)",
                    "price": 10.5,
                    "tax": None,
                },
                {
                    "name": "Pencil",
                    "description": "Made up of Graphite",
                    "price": 5.0,
                    "tax": 0.5,
                },
                {
                    "name": "Eraser",
                    "description": "Made up of Rubber",
                    "price": 3.0,
                    "tax": 0.2,
                }
            ]
        }
    }

@app.put("/items/{item_id}")
async def Item(
    item_id:int, item:Item
):
    result = {"item_id":item_id, "item":item}
    return result