# You can define Header parameters the same way you define Query, Path and Cookie parameters.

from typing import Annotated
from fastapi import FastAPI, Header

app = FastAPI()
@app.get("/items/")
async def read_items(user_agent: Annotated[str |None, Header()] = None):
    return {"User-Agent": user_agent}

# Header is a "sister" class of Path, Query and Cookie. It also inherits from the same common Param class.

# But remember that when you import Query, Path, Header, and others from fastapi, those are actually functions that return special classes.
    
# Header(convert_underscores=False) - you may use this..