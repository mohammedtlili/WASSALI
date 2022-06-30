from fastapi import APIRouter

from models.input_model import Transport
from service.tarification import calcul

router = APIRouter()


@router.get("/hello")
def read_marchandise_by_id():
    return "hello"


@router.post("/calcul")
def input_transport(request_body: Transport):
    return calcul(request_body)

@router.get("/calcul")
def output_transport(request_body: Transport):
    return calcul(request_body)
