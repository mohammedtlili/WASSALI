from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from enum import Enum
from typing import Optional
"""
Importer Basedepuis database
Créez des classes qui en héritent, 
Ces classes sont les modèles SQLAlchemy
"""
from database import Base



class Marchandise(Base):
    __tablename__ = "marchandises"
    id_marchandise = Column(Integer, primary_key=True, index=True)
    nbre_objet = Column(Integer)
    label = Column(String)
    #categorie_vihecule = relationship("Categorie_vihecule", back_populates="Categ_vihecule")

""""
class Categorie_vihecule(Base):
    __tablename__ = "vihecule"
    id_vihecule = Column(Integer, primary_key=True, index=True)

    utilitaire = "Utilitaire"
    camionnette = "Camionnette"
    fourgon = "Fourgon"
    porteur = "Porteur"
"""

class Categorie_vihecule(str, Enum):
    __tablename__ = "categorie_vihecule"
    utilitaire = "Utilitaire"
    camionnette = "Camionnette"
    fourgon = "Fourgon"
    porteur = "Porteur"
    """"
    Categ_vihecule_id = Column(Integer, ForeignKey("marchandises.id"))
    Categ_vihecule_id = Column(Integer, ForeignKey("transports.id"))

    Categ_vihecule = relationship("Marchandise", back_populates="categorie_vihecule")
    Categ_vihecule2 = relationship("Transport", back_populates="categorie_vihecule")
"""
class Transport(Base):
    __tablename__ = "transports"
    id_transport = Column(Integer, primary_key=True, index=True)
    categorie_vihecule : Optional[Categorie_vihecule] = None
    Nombre_km = Column(Float)
    temps_service = Column(Integer)
    prix = Column(Float)
    #categorie_vihecule = relationship("Categorie_vihecule", back_populates="Categ_vihecule2")



