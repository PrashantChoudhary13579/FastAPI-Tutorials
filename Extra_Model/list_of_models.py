from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str

Items = [
    {"name":"Foo","description":"Here's come my hero"},
    {"name":"Red","description":"It's my fav. color."}
]

@app.get("/items/", response_model=list[Item])
async def read_items():
    return Items