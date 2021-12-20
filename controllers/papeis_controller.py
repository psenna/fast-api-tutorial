from fastapi import APIRouter
import ormar
from controllers.utils.delete_controller import delete_controller
from controllers.utils.entidade_nao_encontrada import entidade_nao_encontrada
from controllers.utils.get_all_controller import get_all_controller
from controllers.utils.get_controller import get_controller
from controllers.utils.patch_controller import patch_controller
from controllers.utils.post_controller import post_controller

from models.papel import Papel
from models.requests.papel_update import PapelUpdate

router = APIRouter()

@router.post("/")
@post_controller
async def add_item(entidade: Papel):
    pass

@router.get("/")
@get_all_controller(Papel)
async def list_item():
    pass

@router.get("/{id}")
@get_controller(Papel)
async def get_papel(id: int):    
    pass

@router.patch("/{id}")
@patch_controller(Papel)
async def patch_papel(propriedades_atualizacao: PapelUpdate, id: int):
    pass

@router.delete("/{id}")
@delete_controller(Papel)
async def delete_papel(id: int):
    pass
