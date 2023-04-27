from fastapi import APIRouter

from controllers.utils.delete_controller import delete_controller
from controllers.utils.entidade_nao_encontrada import entidade_nao_encontrada
from controllers.utils.get_all_controller import get_all_controller
from controllers.utils.get_controller import get_controller
from controllers.utils.post_controller import post_controller

from models.cotacao import Cotacao

router = APIRouter()

@router.post("/")
@post_controller
async def add_cotacao(entidade: Cotacao):
    pass

@router.get("/")
@get_all_controller(Cotacao)
async def get_all_cotacoes():
    pass

@router.get("/{id}")
@get_controller(Cotacao, [Cotacao.papel])
async def get_cotacao(id: int):    
    pass

@router.delete("/{id}")
@delete_controller(Cotacao)
async def delete_cotacao(id: int):
    pass
