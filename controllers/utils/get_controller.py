import ormar
from functools import wraps

from controllers.utils.entidade_nao_encontrada import entidade_nao_encontrada


def get_controller(modelo: ormar.Model):
    def inner(func):
        @entidade_nao_encontrada
        @wraps(func)
        async def wrapper(id: int):
            entidade = await modelo.objects.get(id=id)
            return entidade
        return wrapper
    return inner