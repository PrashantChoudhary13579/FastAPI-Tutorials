from pydantic import BaseModel
from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl= "tokens")

class User(BaseModel):
    username: str
    password: str | None = None
    full_name :str |None = None
    disabled: bool | None = None

def fake_decode_token(token):
    return User(
        username = token + "fakedecoded" , email = "john1234@gmail.com", full_name = "John Doe"
    )

async def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)]
):
    user = fake_decode_token(token)
    return user

@app.get("/items/me")
async def read_users_me(
    user:Annotated[User, Depends(get_current_user)]
):
    return user