# You can use Pydantic models to declare form fields in FastAPI.

from fastapi import FastAPI, Form
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

class FormData(BaseModel):
    username: str
    password: str
    model_config={
        "extra":"forbid"
    }
# model config type helps us to find out the error, if the user sends some wrong information
@app.post("/data/")
async def login(data: Annotated[FormData, Form()]):
    return data