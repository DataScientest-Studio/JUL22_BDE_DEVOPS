from fastapi import FastAPI 

app = FastAPI()

@app.get("/hello")
def hello():
    return "Hello"

@app.get("/status")
def stat():
    return 1

@app.get("/data")
def er():
    return {"data":"hello"}

