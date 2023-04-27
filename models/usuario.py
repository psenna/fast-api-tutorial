import ormar
import re
from pydantic import validator

from config import database, metadata

class Usuario(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "usuarios"

    id: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(max_length=100)
    email: str = ormar.String(max_length=100, unique=True)
    hash_password: str = ormar.String(max_length=255)

    @validator('email')
    def valida_formatacao_sigla(cls, v):
        if not re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+').match(v):
            raise ValueError('The user email format is invalid!')
        return v