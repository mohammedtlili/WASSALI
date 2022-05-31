from typing import Union
from fastapi.encoders import jsonable_encoder
#from pydantic import Optional
from typing import Optional
from enum import Enum

import models
import uvicorn
from fastapi import FastAPI, HTTPException, Depends, Body
from pydantic import BaseModel
from models import *
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from . import models, schemas


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


#****************************************************************************************




store_Marchandise = []


@app.post("/transporter/", status_code=201)
def add_marchandise(marchandise: Marchandise, db: Session = Depends(get_db)):
    marchandise_model = models.Marchandise()
    marchandise_model.nbre_objet = marchandise.nbre_objet
    marchandise_model.label = marchandise.label

    db.add(marchandise_model)
    db.commit()
    return marchandise


@app.get("/transporter/")
def read_all_marchandise(db: Session = Depends(get_db)):
    return db.query(models.Marchandise).all()


@app.get("/transporter/{id_marchandise}")
def read_marchandise_by_id(id_marchandise: int):
    try:
        return store_Marchandise[id_marchandise]
    except:
        raise HTTPException(status_code=404, detail="Marchandise n'existe pas")


@app.put("/transporter/{id_marchandise}")
def update_marchandise_by_id(id_marchandise: int, marchandise: Marchandise, db: Session = Depends(get_db)):
    marchandise_model = db.query(models.Marchandise).filter(models.Marchandise.id == id_marchandise).first()

    if marchandise_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID {id_marchandise} : Does not exist"
        )

    marchandise_model = models.Marchandise()
    marchandise_model.nbre_objet = marchandise.nbre_objet
    marchandise_model.label = marchandise.label

    db.add(marchandise_model)
    db.commit()
    return marchandise



#****************************************************************************************************



@app.post("/transporter/{vihecule}/")
def add_Vihecule(vihecule: Categorie_vihecule):
    return {"Hello": vihecule.value}


@app.get("/transporter/{vihecule}/")
def read_all_categorie_vihecule(vihecule: Categorie_vihecule):
    if (vihecule == Categorie_vihecule.utilitaire):
        return {"message": "votre vihecule est utilitaire"}
    elif (vihecule == Categorie_vihecule.camionnette):
        return {"message": "votre vihecule est camionnette"}
    elif (vihecule == Categorie_vihecule.fourgon):
        return {"message": "votre vihecule est fourgon"}
    return {"message": "votre vihecule est porteur"}


""""
store_vihecule = []

@app.post("/transporter/")
def add_categorie_vihecule(categorie_vihecule: Categorie_vihecule):
    store_vihecule.append(categorie_vihecule)
    return categorie_vihecule

@app.get("/transporter/", response_model=list[Categorie_vihecule])
def read_all_categorie_vihecule():
    return store_vihecule

@app.get("/transporter/{id_vihecule}")
def read_categorie_vihecule(id_vihecule: int):
    try:
        return store_vihecule[id_vihecule]
    except:
        raise HTTPException(status_code=404, detail="Categorie vihecule n'existe pas")



@app.put("/transporter/{id_vihecule}")
def update_ategorie_vihecule(id_vihecule: int, new_vihecule: Categorie_vihecule):
    try:
        store_Marchandise[id_vihecule] = new_vihecule
        return store_vihecule[id_vihecule]
    except:
        raise HTTPException(status_code=404, detail="Categorie vihecule n'existe pas")
"""



#**************************************************************************************************
class Transport(BaseModel):
    Nombre_km: float
    temps_service: int
    prix: float


store_Transport = []




@app.post("/transporter/transport/")
def add_transport(transport: Transport, db: Session = Depends(get_db)):
    transport_model = models.Transport()
    transport_model.Nombre_km = transport.Nombre_km
    transport_model.temps_service = transport.temps_service

    db.add(transport_model)
    db.commit()
    return transport

@app.get("/transporter/transports/")
def calcul_prix(transport: Transport, db: Session = Depends(get_db)):
    #transport.prix = transport.Nombre_km * 10
    return db(models.transport.prix) * 10



@app.get("/transporter/transport/")
def read_all_transport(db: Session = Depends(get_db)):
    return db.query(models.Transport).all()


@app.get("/transporter/{id_transport}", status_code=202)
def read_transport_by_id(id_transport: int):
    try:
        return store_Transport[id_transport]
    except:
        raise HTTPException(status_code=404, detail="Transport n'existe pas")


@app.put("/transporter/{id_transport}")
def update_transport_by_id(id_transport: int, new_transport: Transport):
    try:
        store_Transport[id_transport] = new_transport
        return Transport[id_transport]
    except:
        raise HTTPException(status_code=404, detail="Transport n'existe pas")

#******************************************************************************************
@app.get("/")
def read_root():
    return {"application de tarification": "phase de test "}


if __name__ == "__main__":
    uvicorn.run("tariF.py: app")
