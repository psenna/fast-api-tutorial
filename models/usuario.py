import ormar
import re
from pydantic import validator
import pydantic

from config import database, metadata

funcoes_validas = ["admin", "operador", "investidor"]

class Usuario(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "usuarios"

    id: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(max_length=100)
    email: str = ormar.String(max_length=100, unique=True)
    hash_password: str = ormar.String(max_length=255)
    funcoes: pydantic.Json = ormar.JSON(default=[])

    @validator('email')
    def valida_formatacao_sigla(cls, v):
        if not re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+').match(v):
            raise ValueError('O formato do email é inválido!')
        return v

    @validator('funcoes')
    def valida_funcao_existem(cls, v):
        if not isinstance(v, list):
            raise ValueError(f'As funções de um usuário deve ser uma lista!')
        for funcao in v:
            if not isinstance(funcao, str) or funcao not in funcoes_validas:
                raise ValueError(f'A função {funcao} não é um função válida!')
        return v

    @validator('funcoes')
    def remove_funcoes_duplicadas(cls, v):
        return list(set(v))
