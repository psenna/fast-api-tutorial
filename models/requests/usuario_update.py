from typing import Optional
from pydantic import BaseModel, Field, validator
from security import get_password_hash


class UsuarioUpdateRequest(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    hash_password: Optional[str] = Field(alias='password', default=None)

    @validator('hash_password', pre=True)
    def hash_the_password(cls, v):
        if v:
            return get_password_hash(v)
        return v
