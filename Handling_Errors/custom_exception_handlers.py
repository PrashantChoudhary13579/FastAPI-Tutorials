# You can add custom exception handlers with the same exception utilities from Starlette

from fastapi import FastAPI , Request
from fastapi.responses import JSONResponse

class UnicornException(Exception):
    def __init__ (self, name: str):
        self.name = name

router = FastAPI()

@router.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message":f"Oops!!!,{exc.name} did something. There we found rainbow.."}
    )
@router.get("/uvicorns/{name}")
async def read_uvicorn(name:str):
    if name == "yolo" or name=="nolo":
        raise UnicornException(name = name)
    return {"uvicorn_name":name}