from pydantic import BaseModel, EmailStr
from fastapi import FastAPI
from typing import Annotated

app = FastAPI()

class UserIn(BaseModel):
    username : str
    password :str
    email: EmailStr
    full_name: str |None = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str |None = None

class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str |None = None

def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password

def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(UserIn.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User saved... ")
    return user_in_db

@app.post("/user/", response_model = True)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved