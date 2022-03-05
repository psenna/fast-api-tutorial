from typing import List
from fastapi import APIRouter, Depends, Form, HTTPException
from controllers.depends.usuario import get_user_com_funcao, get_usuario_logado
from controllers.utils.delete_controller import delete_controller
from controllers.utils.entidade_nao_encontrada import entidade_nao_encontrada
from controllers.utils.get_all_controller import get_all_controller
from controllers.utils.get_controller import get_controller
from controllers.utils.patch_controller import patch_controller
from controllers.utils.requisitar_usuario_com_funcao import requisitar_usuario_com_funcao
from models.requests.usuario_update import UsuarioUpdateRequest
from models.requests.usuario_create import UserCreateRequest
from models.responses.usuario_response import UsuarioResponse

from models.usuario import Usuario
from security import criar_token_jwt, verify_password

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
async def get_papel(id: int, 
    usuario_logado: Usuario = Depends(get_usuario_logado)):    
    pass

@router.patch("/{id}", response_model=UsuarioResponse)
@patch_controller(Usuario)
async def patch_papel(propriedades_atualizacao: UsuarioUpdateRequest, id: int):
    pass

@router.delete("/{id}")
@delete_controller(Usuario)
@requisitar_usuario_com_funcao(funcoes=['admin'])
async def delete_papel(id: int):
    pass

@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    user = await Usuario.objects.get_or_none(email=username)
    if not user or not verify_password(password, user.hash_password):
        raise HTTPException(status_code=403,
                            detail="Email ou nome de usuário incorretos"
                           )
    return {
        "access_token": criar_token_jwt(user.id),
        "token_type": "bearer",
    }

@router.post("/{id}/funcoes/{funcao}", response_model=UsuarioResponse)
@entidade_nao_encontrada
async def add_funcao_usuario(id: int, funcao: str):
    usuario = await Usuario.objects.get(id=id)
    usuario.funcoes.append(funcao)
    await usuario.update()
    return usuario

@router.delete("/{id}/funcoes/{funcao}", response_model=UsuarioResponse)
@entidade_nao_encontrada
async def delete_funcao_usuario(id: int, funcao: str):
    usuario = await Usuario.objects.get(id=id)
    usuario.funcoes.remove(funcao)
    await usuario.update()
    return usuario