from typing import Dict
from security import get_password_hash, verify_password, criar_token_jwt
from models.usuario import Usuario

class UsuarioFactory():
    @classmethod
    def get_prorpiedades_validas(cls, props:Dict = {}):
        default_props = {
            "id": 0,
            "nome": "Nome pessoa",
            "email": "pessoa@email.com",
            "hash_password": get_password_hash("password"),
        }

        return {**default_props, **props}


    @classmethod
    def get_requisicao_validas(cls, props:Dict = {}):
        default_props = {
            "id": 0,
            "nome": "Nome pessoa",
            "email": "pessoa@email.com",
            "password": "password",
        }

        return {**default_props, **props}

    
    @classmethod
    async def create(cls, props:Dict = {}) -> Usuario:
        new_user = Usuario(**cls.get_valid_user_properties(props=props))
        await new_user.save()
        return new_user

    @classmethod
    async def get_usuario_token_headers(cls, papeis=[]):
        props = {'is_superuser': True, 'email': 'superuser@mail.com'}
        usuario = Usuario(**cls.get_valid_user_properties(props=props))
        usuario.papeis = papeis
        await usuario.save()
        token = criar_token_jwt(usuario.id)
        return {"Authorization": f"Bearer {token}"}


    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str):
        return verify_password(plain_password, hashed_password)