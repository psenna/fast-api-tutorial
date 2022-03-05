from typing import List
from pydantic import BaseModel


class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    funcoes: List[str]