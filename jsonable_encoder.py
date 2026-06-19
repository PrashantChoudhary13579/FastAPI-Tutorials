from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from datetime import datetime

fake_db = {}

class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str |None = None

app = FastAPI()
@app.put('/items/{id}')
async def update_item(id: str, item:Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
    # data = jsonable_encoder(item)

    # print(data)
    # print(type(data))

    return {"id":id, "item":item}