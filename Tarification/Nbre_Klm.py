from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()


class marchandise(BaseModel):
    nbre_objet: int
    label: str
    marchandise_id: int

@app.get("/marchandises}")
def read_marchandise(marchandise_id: int, nbre_objet: int, label: str):
    return {"marchandise_id": marchandise_id, "nbre_objet": nbre_objet, "Label": label}

@app.put("/marchandises}")
def update_marchandise(marchandise_id: int, nbre_objet: int, label: str):
    return {"marchandise_id": marchandise_id, "nbre_objet": nbre_objet, "Label": label}

@app.post("/marchandises}")
def input_marchandise(marchandise_id: int, nbre_objet: int, label: str):
    return {"marchandise_id": marchandise_id, "nbre_objet": nbre_objet, "Label": label}

class categorie_vihecule(BaseModel):
    id_categorie_vihecule: int

class categorie(Enum):
    utilitaire = 1
    camionnette = 2
    fourgon = 3
    porteur = 4


@app.get("/categorie_vihecule")
def input_categorie_vihecule(id_categorie_vihecule: int, categorie: Enum):
    return {"id_categorie_vihecule": id_categorie_vihecule, "Categorie": categorie}

@app.post("/categorie_vihecule}")
def output_categorie_vihecule(id_categorie_vihecule: int, categorie: Enum):
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




