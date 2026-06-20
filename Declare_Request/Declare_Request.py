from fastapi import FastAPI
from pydantic import BaseModel, Field   

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str|None = Field(default=None,examples= ["A very nice Item"] )
    price: float = Field(examples=[34.5])
    tax : float |None = Field(default=None, examples=[3.2])
    model_config={
        "json_schema_extra":{
            "example":
                {
                    "name" : "chalk",
                    "description": "Made up of CaCO3 (Calicum Carbonate)",
                    "price":10.5,
                    "tax":None,
                    
                }
            
        }
    }

@app.put("/item/{item_id}")
async def update_item(item_id:int, item:Item):
    results = {"item_id":item_id, "item":item}
    return results

# For single example using model_config...it declare the request..