from typing import List
from fastapi import APIRouter
from controllers.utils.delete_controller import delete_controller
from controllers.utils.get_all_controller import get_all_controller
from controllers.utils.get_controller import get_controller
from controllers.utils.patch_controller import patch_controller
from models.requests.usuario_update import UsuarioUpdateRequest
from models.requests.usuario_create import UserCreateRequest
from models.responses.usuario_response import UsuarioResponse

from models.usuario import Usuario

router = APIRouter()

@router.post("/", response_model=UsuarioResponse)
async def add_item(create_request: UserCreateRequest):
    atributos = create_request.dict(exclude_unset=True)
    usuario = Usuario(**atributos)
    return await usuario.save()

@router.get("/", response_model=List[UsuarioResponse])
@get_all_controller(Usuario)
async def list_item():
    pass

@router.get("/{id}", response_model=UsuarioResponse)
@get_controller(Usuario)
async def get_papel(id: int):    
    pass

@router.patch("/{id}", response_model=UsuarioResponse)
@patch_controller(Usuario)
async def patch_papel(propriedades_atualizacao: UsuarioUpdateRequest, id: int):
    pass

@router.delete("/{id}")
@delete_controller(Usuario)
async def delete_papel(id: int):
    pass