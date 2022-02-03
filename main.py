from typing import Optional
from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
def read_root():
    return("Welcome to the Pokedex API!")

@app.get("/api/pokedex/")
def pokedex_all():
    with open('./pokedex/pokedex.json', 'rb') as f:
        data = json.load(f)
    return data["pokedex"]

@app.get("/api/pokedex/{json_number}")
async def pokedex(
    json_number :int,
    id :Optional[bool] = None,
    name :Optional[bool] = None,
    classification :Optional[bool] = None,
    height :Optional[bool] = None,
    weight :Optional[bool] = None,
    mega_evolution :Optional[bool] = None,
    mega_evolution_name :Optional[bool] = None,
    mega_evolution_height :Optional[bool] = None,
    mega_evolution_weight :Optional[bool] = None,
    mega_evo_name :Optional[bool] = None,
    mega_evo_height :Optional[bool] = None,
    mega_evo_weight :Optional[bool] = None
    ):

    json_number -= 1
    print(f"request_id:{json_number + 1}")

    with open('./pokedex/pokedex.json', 'rb') as f:
        data = json.load(f)

    if id is True:
        response = data["pokedex"][json_number]["id"]
    elif name is True:
        response = data["pokedex"][json_number]["name"]
    elif classification is True:
        response = data["pokedex"][json_number]["classification"]
    elif height is True:
        response = data["pokedex"][json_number]["height"]
    elif weight is True:
        response = data["pokedex"][json_number]["weight"]
    else:
        response = "Not Found."

    if mega_evolution is True:
        response = data["pokedex"][json_number]["mega_evolution"][0]
    elif mega_evolution_name is True or mega_evo_name is True:
            response = data["pokedex"][json_number]["mega_evolution"][0]["name"]
    elif mega_evolution_height is True or mega_evo_height is True:
            response = data["pokedex"][json_number]["mega_evolution"][0]["height"]
    elif mega_evolution_weight is True or mega_evo_weight is True:
            response = data["pokedex"][json_number]["mega_evolution"][0]["weight"]
    else:
        response = "Not Found."

    return response

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#    return {"item_id": item_id, "q": q}