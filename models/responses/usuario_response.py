from pydantic import BaseModel


class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str