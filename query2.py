from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id:str, item_id: str, q: str|None = None, short:bool = False
):
    item = {"item_id":item_id, 'owner_id':user_id}
    if q:
        item.update({"q" :q})
    if not short:
        item.update({"Description": "We are learning something new each and every day.."})
    return item

# http://localhost:8000/users/5/items/foo?short=0
# http://127.0.0.1:8000/users/1/items/foo?short=0

# Both of them are working correctly.. 
