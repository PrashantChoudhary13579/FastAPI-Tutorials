from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

fake_user_db ={
    "john":{
        "username":"johndoe",
        "full_name":"John Doe", 
        "email":"johndoe1234@gmail.com",
        "hashed_password":"fakesecret",
        "disabled":False,
    },
    "alice":{
        "username":"alice",
        "full_name":"Alice in Wonderland",
        "email":"alice@example.com",
        "hashed_password":"fakesecret2",
        "disabled":True,
    },
}

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="Token")

def fake_hash_password(password: str):
    return "fakehashed" + password

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str |None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

def get_user(db, username:str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    user = get_user(fake_user_db, token)
    return user

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail = "Not Authentic user",
            headers={"WWW-Authenticate":"Bearer"}, 
        )
    return user

async def get_current_active_user(
    current_user:Annotated[ User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "Not Active")
    return current_user

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_user_db.get(form_data.username)
    if not user_dict :
        raise HTTPException(status_code=400, detail = "Incorrect username or password")
    user = UserInDB(**user_dict)
    hass_password = fake_hash_password(form_data.password)
    if not hass_password == user.hashed_password: 
        raise HTTPException(status_code = 400, detail = "Incorrect username or password")
    
    return {"username":user.username, "token_type": "Bearer "}

@app.get("/users/me")
async def read_user_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user