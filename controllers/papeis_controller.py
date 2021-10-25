from typing import List
from fastapi import APIRouter

from models.papel import Papel

router = APIRouter()

@router.post("/", response_model=Papel)
async def add_item(papel: Papel):
    await papel.save()
    return papel

@router.get("/", response_model=List[Papel])
async def list_item():
    return await Papel.objects.all()