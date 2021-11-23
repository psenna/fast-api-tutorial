from fastapi.testclient import TestClient
from models.papel import Papel
from tests.utils.papeis import create_papel_invalido, create_papel_valido
import asyncio

def test_cria_papel(client: TestClient) -> None:
    body = create_papel_valido()
    response = client.post("/papeis/", json=body)
    content = response.json()
    assert response.status_code == 200
    assert content["cnpj"] == body["cnpj"]

def test_cria_papel_com_sigla_invalida(client: TestClient) -> None:
    body = create_papel_invalido(['sigla'])
    response = client.post("/papeis/", json=body)
    content = response.json()
    assert response.status_code == 422

def test_obtem_um_papel_por_id(client: TestClient) -> None:
    atributos = create_papel_valido()
    papel = Papel(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(papel.save())

    response = client.get(f"/papeis/{papel.id}")
    content = response.json()

    assert response.status_code == 200
    assert content["sigla"] == papel.sigla

def test_obtem_papel_inexistente_por_id(client: TestClient) -> None:
    response = client.get(f"/papeis/1")
    content = response.json()

    assert response.status_code == 404
    assert content["mensagem"] == "Entidade não encontrada"
