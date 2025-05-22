from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello, world!"}


@app.get("/bye")
def hello():
    return {"message": "Bye, world!"}
