import enum

from pydantic import BaseModel
from enum import Enum
from sqlalchemy import Column, Integer, String, Float


class Categorie(Enum):
    utilitaire = "utilitaire"
    fourgon = "fourgon"
    porteur = "porteur"
    camionette = "camionette"


class Transport(BaseModel):
    __tablename__ = "Transport"
    nmbre_km = Column(int)
    temps_service = Column(float)
    categorie = Column(Categorie)
    prix = Column(float)



class Marchandise(BaseModel):
    __tablename__ = "Marchandise"
    prix_min = Column(float)
    prix_max = Column(float)
    #nbre_objet: int
    #label: str
#
# class Marchandise(BaseModel):
#     nbre_objet: int
#     label: str
