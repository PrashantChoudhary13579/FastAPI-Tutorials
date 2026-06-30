# You can define Cookie parameters the same way you define Query and Path parameters.

from typing import Annotated
from fastapi import Cookie, FastAPI
app = FastAPI()

@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return { "ads_id": ads_id }


# Cookie is a "sister" class of Path and Query. It also inherits from the same common Param class.

# But remember that when you import Query, Path, Cookie and others from fastapi, those are actually functions that return special classes.