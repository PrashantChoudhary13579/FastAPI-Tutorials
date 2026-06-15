# Note: You can use Pydantic Model to declare query parameters in FastAPI...

from typing import Annotated, Literal
from fastapi import FastAPI , Query
from pydantic import BaseModel, Field

app = FastAPI()

class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, lt=100)
    offset:int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []

@app.get("/Items/")
async def read_items(
    filter_query: Annotated[FilterParams, Query()]):
    return filter_query
