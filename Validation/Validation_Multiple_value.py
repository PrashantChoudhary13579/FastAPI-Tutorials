from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: Annotated[ 
        list[str]|None, 
        Query(
            alias= "items-query",
            title="Query string", 
            max_length=50,
            min_length=3, # representing the count of the list
            description="Query string for the items to search in the database that have a good match",
            pattern="^fixedquery$",
            deprecated=True # shows - Internal Server Error
        )] = None
):
    query_items = {"q":q}
    return query_items

# You can also provide a default list is none is provided and you want it.. just replace the list with None

# There are more parameters that can be used.. like - title, description