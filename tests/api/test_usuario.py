from fastapi.testclient import TestClient
from models.usuario import Usuario
from tests.utils.usuario import create_usuario_valido, create_requisicao_usuario_valida
import asyncio
import pytest
import ormar

def test_lista_todos_os_usuarios(client: TestClient) -> None:
    atributos = create_usuario_valido()
    usuario = Usuario(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(usuario.save())
    
    response = client.get("/usuarios/")
    content = response.json()

    assert response.status_code == 200
    assert len(content) == 1

def test_cria_usuario(client: TestClient) -> None:
    body = create_requisicao_usuario_valida()

    response = client.post("/usuarios/", json=body)
    
    content = response.json()
    assert response.status_code == 200
    assert content["nome"] == body["nome"]

def test_obtem_uma_cotacao_por_id(client: TestClient) -> None:
    atributos = create_usuario_valido()
    usuario = Usuario(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(usuario.save())

    response = client.get(f"/usuarios/{usuario.id}")
    content = response.json()

    assert response.status_code == 200
    assert content["nome"] == usuario.nome

def test_delete_usuario_existente(client: TestClient) -> None:
    atributos = create_usuario_valido()
    usuario = Usuario(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(usuario.save())

    response = client.delete(f"/usuarios/{usuario.id}")

    with pytest.raises(ormar.exceptions.NoMatch): 
        loop.run_until_complete(Usuario.objects.get(id=usuario.id))

    assert response.status_code == 200
