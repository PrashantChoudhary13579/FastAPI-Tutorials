from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class Tags(Enum):
    items ='items'
    users = 'users'

@app.get('/items/', tags = [Tags.items])
async def read_item():
    return ['Portal gun', 'Plumbus']

@app.get('/users/', tags = [Tags.items])
async def read_users():
    return ["Rick","Monty"]