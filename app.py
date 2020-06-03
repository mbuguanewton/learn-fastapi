from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
def index():
    return {"say": "Hello world"}


@app.get("/post/{name}")
def add(name):
    return {"post": f"you added the name {name}"}
