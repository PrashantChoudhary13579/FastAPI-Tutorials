from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"item_name":"foo"},
    {"item_name":"bar"},
    {"item_name":"bak"}
]
@app.get("/Items/")
async def read_items(skip: int=0, limit:int =10):
    return fake_items_db[skip:skip+limit]