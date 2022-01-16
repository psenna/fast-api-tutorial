import ormar
from functools import wraps

from controllers.utils.entidade_nao_encontrada import entidade_nao_encontrada


def get_all_controller(modelo: ormar.Model):
    def inner(func):
        @wraps(func)
        async def wrapper():
                return await modelo.objects.all()
        return wrapper
    return inner