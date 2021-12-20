from functools import wraps
import ormar

from controllers.utils.entidade_nao_encontrada import entidade_nao_encontrada

def delete_controller(modelo: ormar.Model):
    def inner(func):
        @entidade_nao_encontrada
        @wraps(func)
        async def wrapper(id: int):
            entidade = await modelo.objects.get(id=id)
            return await entidade.delete()
        return wrapper
    return inner