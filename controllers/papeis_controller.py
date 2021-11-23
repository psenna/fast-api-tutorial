from fastapi import APIRouter, Response
import ormar

from models.papel import Papel

router = APIRouter()

@router.post("/")
async def add_item(papel: Papel):
    await papel.save()
    return papel

@router.get("/")
async def list_item():
    return await Papel.objects.all()

@router.get("/{papel_id}")
async def get_papel(papel_id: int, response: Response):
    try:
        papel = await Papel.objects.get(id=papel_id)
        return papel
    except ormar.exceptions.NoMatch:
        response.status_code = 404
        return {"mensagem": "Entidade não encontrada"}
