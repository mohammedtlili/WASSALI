from typing import Union
from fastapi.encoders import jsonable_encoder

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum
from fastapi import FastAPI, Body

# from pydantic import Optional
from typing import Optional

app = FastAPI()


class Marchandise(BaseModel):
    id_marchandise: int
    nbre_objet: int
    label: str


store_Marchandise = []


@app.post("/marchandise/")
def add_marchandise(marchandise: Marchandise):
    store_Marchandise.append(marchandise)
    return marchandise


@app.get("/marchandise/", response_model=list[Marchandise])
def read_all_marchandise():
    return store_Marchandise


@app.get("/marchandise/{id_marchandise}")
def read_marchandise(id_marchandise: int):
    try:
        return store_Marchandise[id_marchandise]
    except:
        raise HTTPException(status_code=404, detail="Marchandise n'existe pas")


@app.put("/marchandise/{id_marchandise}")
def update_marchandise(id_marchandise: int, new_marchandise: Marchandise):
    try:
        store_Marchandise[id_marchandise] = new_marchandise
        return store_Marchandise[id_marchandise]
    except:
        raise HTTPException(status_code=404, detail="Marchandise n'existe pas")


class Categorie_vihecule(str, Enum):
    utilitaire = "Utilitaire"
    camionnette = "Camionnette"
    fourgon = "Fourgon"
    porteur = "Porteur"


@app.post("/Vihecule/{vihecule}/")
def add_Vihecule(vihecule: Categorie_vihecule):
    return {"Hello": vihecule.value}


@app.get("/Vihecule/{vihecule}/")
def read_all_categorie_vihecule(vihecule: Categorie_vihecule):
    if (vihecule == Categorie_vihecule.utilitaire):
        return {"message": "votre vihecule est utilitaire"}
    elif (vihecule == Categorie_vihecule.camionnette):
        return {"message": "votre vihecule est camionnette"}
    elif (vihecule == Categorie_vihecule.fourgon):
        return {"message": "votre vihecule est fourgon"}
    return {"message": "votre vihecule est porteur"}


"""""
store_vihecule = []

@app.post("/vihecule/")
def add_categorie_vihecule(categorie_vihecule: Categorie_vihecule):
    store_vihecule.append(categorie_vihecule)
    return categorie_vihecule

@app.get("/vihecule/", response_model=list[Categorie_vihecule])
def read_all_categorie_vihecule():
    return store_vihecule

@app.get("/vihecule/{id_vihecule}")
def read_categorie_vihecule(id_vihecule: int):
    try:
        return store_vihecule[id_vihecule]
    except:
        raise HTTPException(status_code=404, detail="Categorie vihecule n'existe pas")



@app.put("/vihecule/{id_vihecule}")
def update_ategorie_vihecule(id_vihecule: int, new_vihecule: Categorie_vihecule):
    try:
        store_Marchandise[id_vihecule] = new_vihecule
        return store_vihecule[id_vihecule]
    except:
        raise HTTPException(status_code=404, detail="Categorie vihecule n'existe pas")
"""


class Transport(BaseModel):
    id_transport: int
    Nombre_km: float
    temps_service: int
    prix: float


store_Transport = []


@app.post("/Transport/")
def add_transport(transport: Transport):
    store_Transport.append(transport)

    return transport


@app.get("/Transport/", response_model=list[Transport])
def read_all_transport():
    return (store_Transport)


@app.get("/Transport/{id_transport}")
def read_transport(id_transport: int):
    try:
        return store_Transport[id_transport]
    except:
        raise HTTPException(status_code=404, detail="Transport n'existe pas")


@app.put("/Transport/{id_transport}")
def update_transport(id_transport: int, new_transport: Transport):
    try:
        store_Transport[id_transport] = new_transport
        return Transport[id_transport]
    except:
        raise HTTPException(status_code=404, detail="Transport n'existe pas")


@app.get("/")
def read_root():
    return {"application de tarification": "phase de test "}


if __name__ == "__main__":
    uvicorn.run("Nbre_Klm.py: app")
