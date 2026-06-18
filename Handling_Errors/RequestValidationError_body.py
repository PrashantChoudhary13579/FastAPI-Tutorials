from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

# this will automatically run when create_item do not get the correct input.. 
@app.exception_handler(RequestValidationError)
async def valid_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content= jsonable_encoder({"detail":exc.errors(), "body":exc.body})
    )

class Item(BaseModel):
    title: str
    size: int

@app.post("/items/")
async def create_item(item:Item):
    return item