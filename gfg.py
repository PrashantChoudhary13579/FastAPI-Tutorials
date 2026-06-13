from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "I like learning fastapi"
    }

@app.post("/greet")
def greet_user(name, str):
    return {
        "message" : "Hello, " + {name} 
    }