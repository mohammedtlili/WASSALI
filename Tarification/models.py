from sqlalchemy import Column, Integer, String, Float
from database import Base


class Marchandise(Base):
    __tablename__ = "marchandises"
    id_marchandise= Column(Integer, primary_key=True, index=True)
    nbre_objet = Column(Integer)
    label = Column(String)


class Categorie_vihecule(Base):
    __tablename__ = "vihecule"
    id_vihecule = Column(Integer, primary_key=True, index=True)

    utilitaire = "Utilitaire"
    camionnette = "Camionnette"
    fourgon = "Fourgon"
    porteur = "Porteur"



class Transport(Base):
    __tablename__ = "transports"
    id_transport = Column(Integer, primary_key=True, index=True)
    Nombre_km = Column(Float)
    temps_service = Column(Integer)
    prix = Column(Float)


