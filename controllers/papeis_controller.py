from fastapi import APIRouter

from models.papel import Papel

router = APIRouter()

banco_de_dados = []

@router.post("/")
def add_item(item: Papel):
    banco_de_dados.append(item)
    return item

@router.get("/")
def list_item():
    return banco_de_dados