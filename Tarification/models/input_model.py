import enum

from pydantic import BaseModel
from enum import Enum


class Categorie(Enum):
    utilitaire = "utilitaire"
    fourgon = "fourgon"
    porteur = "porteur"
    camionette = "camionette"


class Transport(BaseModel):
    nmbre_km: int
    temps_service: float
    categorie: Categorie
    prix: float


class Marchandise(BaseModel):
    prix_min: float
    prix_max: float
    #nbre_objet: int
    #label: str
#
# class Marchandise(BaseModel):
#     nbre_objet: int
#     label: str
