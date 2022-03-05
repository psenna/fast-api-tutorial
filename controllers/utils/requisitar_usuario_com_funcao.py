import inspect
from functools import wraps
from itertools import count
from typing import List
from fastapi import Depends

from controllers.depends.usuario import get_user_com_funcao
from models.usuario import Usuario


def requisitar_usuario_com_funcao(funcoes:List[str] = []):
    def wrapper(func):
        oldsig = inspect.signature(func)
        params = list(oldsig.parameters.values())
        params_sem_usuario_logado = [param for param in params if param.name != 'usuario_logado']
        possui_usuario_logado = len(params) != len(params_sem_usuario_logado)
        newparam = inspect.Parameter('usuario_logado',
                        inspect.Parameter.KEYWORD_ONLY,
                        default = Depends(get_user_com_funcao(funcoes=funcoes)))
        params_sem_usuario_logado.insert(len(params_sem_usuario_logado),newparam)
        sig = oldsig.replace(parameters = params_sem_usuario_logado)

        @wraps(func)
        async def inner(usuario_logado: Usuario, *args, **kwargs):
            if possui_usuario_logado:
                return await func(usuario_logado=usuario_logado, *args, **kwargs)
            return await func(*args, **kwargs)
        inner.__signature__ = sig
        return inner
    return wrapper