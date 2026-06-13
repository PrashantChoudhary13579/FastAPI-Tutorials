from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
async def read_user_1():
    return ["Rick","Monty"]

@app.get("/users")
async def read_user_2():
    return ["Bean","Ravi"]