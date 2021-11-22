from fastapi.testclient import TestClient
from models.papel import Papel
from tests.utils.papeis import create_papel_invalido, create_papel_valido

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

