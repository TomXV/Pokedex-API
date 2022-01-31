from plistlib import load
from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/pokedex/{id}")
def pokedex(id:int):
    id -= 1
    print(id)
    with open('./pokedex/pokedex.json', 'rb') as f:
        data = json.load(f)
    return data["pokedex"][id]

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#    return {"item_id": item_id, "q": q}