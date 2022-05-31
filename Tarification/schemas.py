from enum import Enum

from pydantic import BaseModel


class Marchandise(BaseModel):
    nbre_objet: int
    label: str

class Categorie_vihecule(str, Enum):

    utilitaire = "Utilitaire"
    camionnette = "Camionnette"
    fourgon = "Fourgon"
    porteur = "Porteur"


class Transport(BaseModel):
    Nombre_km: float
    temps_service: int
    prix: float
