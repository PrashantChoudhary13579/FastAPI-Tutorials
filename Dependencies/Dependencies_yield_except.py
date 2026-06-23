from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

class InternalError(Exception):
    pass

def get_username():
    try:
        yield "Rick"
    except InternalError:
        print("Oops!, we didn't raise again, Britney")

@app.get("/items/{item_id}")
async def read_item(item_id: str, username: Annotated[str, Depends(get_username)]):
    if item_id == "portal-gun":
        raise InternalError(
            f"The portal gun is too dangerous to be owned by {username}"
        )
    if item_id!= "plumbus":
        raise HTTPException(status_code=404, detail="Item not found, there's only one plumbus here")
    return  item_id