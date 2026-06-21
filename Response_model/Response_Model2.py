from fastapi import FastAPI
from pydantic import BaseModel,EmailStr
from typing import Any

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str |None = None

class UserOut(BaseModel):
    username: str
    email : EmailStr
    full_name: str

@app.post("/user/", response_model=UserOut)
async def create_user(user:UserIn) -> Any:
    return user


# This is important for securing the password
# response_model or Return Type
# In this case, because the two models are different, if we annotated the function return type as UserOut, the editor and tools would complain that we are returning an invalid type, as those are different classes.