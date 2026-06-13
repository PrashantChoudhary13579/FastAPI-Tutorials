from fastapi import FastAPI

app = FastAPI()

# post - to push some info on to the server
@app.get("/") # to get some info from the server
def hello():
    return {
        'message':'Hello world'
    }

@app.get("/about")
def about():
    return{
        'message':"Now we are learning fastapi"
    }