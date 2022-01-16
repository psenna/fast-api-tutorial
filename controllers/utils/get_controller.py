import ormar
from functools import wraps

from controllers.utils.entidade_nao_encontrada import entidade_nao_encontrada


def get_controller(modelo: ormar.Model, select_related=[]):
    def inner(func):
        @entidade_nao_encontrada
        @wraps(func)
        async def wrapper(id: int):
            consulta = modelo.objects
            if len(select_related):
                consulta = consulta.select_related(select_related)
            entidade = await consulta.get(id=id)
            return entidade
        return wrapper
    return inner