import ormar
from functools import wraps
from pydantic import BaseModel

from controllers.utils.entidade_nao_encontrada import entidade_nao_encontrada 

def patch_controller(modelo: ormar.Model):
    def inner(func):
        @entidade_nao_encontrada
        @wraps(func)
        async def wrapper(propriedades_atualizacao: BaseModel, id: int):
                entidade_salva = await modelo.objects.get(id=id)
                propriedades_atualizadas = propriedades_atualizacao.dict(exclude_unset=True)
                await entidade_salva.update(**propriedades_atualizadas)
                return entidade_salva
        return wrapper
    return inner