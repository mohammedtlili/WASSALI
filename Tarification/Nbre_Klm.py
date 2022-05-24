from typing import Union

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from enum import Enum


db = []

app = FastAPI()


class Marchandise(BaseModel):
    id_marchandise: int
    nbre_objet: int
    label: str

@app.get('/detection')
def get_detections():
    return db
@app.post("/detection")
def add_marchandise(marchandise: Marchandise):
    db.append(marchandise.dict)
    return db[-1]

@app.get("/detection/{id_marchandise}")
def read_marchandise(id_marchandise: int):
    marchandise = id_marchandise-1
    return db[marchandise]

@app.put("/marchandises/{id_marchandise}")
def update_marchandise(id_marchandise: int, marchandise: Marchandise):
    db[id] = marchandise
    return {"message": "operation bien determinée"}



class categorie_vihecule(BaseModel):
    id_categorie_vihecule: int

class categorie(Enum):
    utilitaire = 1
    camionnette = 2
    fourgon = 3
    porteur = 4


@app.get("/categorie_vihecule")
def read_categorie_vihecule(id_categorie_vihecule: int, categorie: Enum):
    return {"id_categorie_vihecule": id_categorie_vihecule, "Categorie": categorie}

@app.post("/categorie_vihecule}")
def input_categorie_vihecule(id_categorie_vihecule: int, categorie: Enum):
    return {"id_categorie_vihecule": id_categorie_vihecule, "Categorie": categorie}

@app.put("/categorie_vihecule")
def update_marchandise(id_categorie_vihecule: int, categorie: Enum):
    return {"id_categorie_vihecule": id_categorie_vihecule, "Categorie": categorie}


class transport(BaseModel):
    id_transport: int
    Nombre_km: float
    temps_service: int
    prix: float

@app.get("/transport}")
def read_transport(id_transport: int, Nombre_km: float, temps_service: int, prix: float):
    prix = Nombre_km *2
    return {"id_transport": id_transport, "Le prix ": prix}

@app.put("/transport}")
def update_transport(id_transport: int, Nombre_km: float, temps_service: int):
    return {"id_transport": id_transport, "Nombre de Klm": Nombre_km, "Le temps de service ": temps_service}

@app.post("/transport}")
def output_transport(id_transport: int, Nombre_km: float, temps_service: int):
    return {"id_transport": id_transport, "Nombre de Klm": Nombre_km, "Le temps de service ": temps_service}




@app.get("/")
def read_root():
    return {"application de tarification": "phase de test "}




