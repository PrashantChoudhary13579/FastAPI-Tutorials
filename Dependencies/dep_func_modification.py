from typing import Annotated
from fastapi import FastAPI, Depends

app = FastAPI()

async def common_parameters(q:str|None = None, skip: int=0, limit:int =100):
    return {"q":q, "skip":skip, "limit":limit}

common_dep = Annotated[dict, Depends(common_parameters)]

@app.get('/items/')
async def read_items(commons:common_dep):
    return commons

@app.get('/users/')
async def read_users(commons:common_dep):
    return commons