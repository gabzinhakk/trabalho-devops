from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/hello world")
async def root():
    return {"message": "Hello World"}


@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": True, "num-aleatorio": random.randint(0, 20000)} 