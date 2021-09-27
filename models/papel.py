from pydantic import BaseModel

class Papel(BaseModel):
    id: int
    nome: str
    sigla: str
    cnpj: str