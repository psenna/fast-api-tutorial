import ormar
from functools import wraps

def post_controller (func):
    @wraps(func)
    async def wrapper(entidade: ormar.Model, **kwargs):
            await entidade.save()
            return entidade
    return wrapper
