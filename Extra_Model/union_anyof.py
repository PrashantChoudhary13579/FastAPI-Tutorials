from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BaseItem(BaseModel):
    description: str
    type: str

class CarItem(BaseItem):
    type: str="car"

class PlaneItem(BaseItem):
    type: str="plane"
    size:int

items ={
    "item1":{"description":"All my friends drive ", "type" : "car"},
    "item2":{
        "description":"Music is my aeroplane, it's my aeroplane",
        "type":"plane",
        "size":5,
    }
}
@app.post("/item/{item_id}", response_model= PlaneItem | CarItem)
async def read_item(item_id:str):
    return items[item_id]
