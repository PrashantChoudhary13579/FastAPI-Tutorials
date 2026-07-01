from typing import Annotated
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/items/")
async def read_items(X_tokens: Annotated[list[str] | None , Header()] = None):
    return {"X-Token values": X_tokens}