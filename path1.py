from fastapi import FastAPI
app = FastAPI()

@app.get("/items/{item_id},{name}")
async def read_item(item_id:int,name:str):
    return {
        "item_id":item_id,
        "item_name":name
    }

@app.get("/items/{item_id}")
async def read_1item(item_id):
    return{
        "item_id":item_id
    }