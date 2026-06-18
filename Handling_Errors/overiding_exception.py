from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

# Override the HTTPException error handler
# this will be executed by overridding the HTTPException .. when item_id == 3..
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


# This function will work when you get a data which is not of the type as describe in read_item (here, int).. 
# At that time this exception handler will be raised automatically
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    message = "Validation Errors: "
    for error in exc.errors():
        message += f"\n Field: {error['loc']}, Error: {error['msg']}"
    return PlainTextResponse(message, status_code = 400)

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail=" Nope.. I don't like 3")
    return {"item_id":item_id}