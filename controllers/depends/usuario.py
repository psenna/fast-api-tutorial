from typing import List, Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import BaseModel, ValidationError

from models.usuario import Usuario
from security import SECRET_KEY, JWT_ALGORITHM


class TokenPayload(BaseModel):
    sub: Optional[int] = None

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl="/usuarios/login"
)

async def get_usuario_logado(
    token: str = Depends(reusable_oauth2)
) -> Usuario:
    try:
        payload = jwt.decode(
            token, SECRET_KEY, algorithms=[JWT_ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = await Usuario.objects.get_or_none(id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_user_com_funcao(funcoes:List[str]=[]):
    def inner(usuario_logado: Usuario = Depends(get_usuario_logado)) -> Usuario:
        if not len(funcoes):
            return usuario_logado
        
        for funcao in funcoes:
            if funcao in usuario_logado.funcoes:
                return usuario_logado

        raise HTTPException(
            status_code=403, detail="O usuário não possui permissão para realizar essa ação!"
        )
    return inner
    
