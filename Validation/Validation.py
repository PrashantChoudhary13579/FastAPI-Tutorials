from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

@app.get("/Items/")
# using Annotated and adding more validation to it..
async def read_items(
    q: Annotated[str|None, Query(min_length=3, max_length=50)] = "Hello"
# pattern="^fixedquery$" - inside Query
):
    # we can also change this .. default value None by replacing it with some another value.. 
    results = {"items": [{ "items_id":"Foo"},{ "items_id":"Baa"}]}
    if q:
        results.update({"q":q})
    return results

# declaring None is much better than declaring a default value