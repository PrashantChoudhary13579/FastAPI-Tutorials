from fastapi import FastAPI, HTTPException

app = FastAPI()

items={"foo":" Foo is a Wrestler.."}

@app.get("/items-header/{item_id}")
async def read_item_head(item_id:str):
    if item_id not in items:
        raise HTTPException(
            status_code=404, 
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item":items[item_id]}

# There are some situations in where it's useful to be able to add custom headers to the HTTP error. For example, for some types of security.