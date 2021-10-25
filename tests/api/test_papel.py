from fastapi.testclient import TestClient

from tests.utils.papeis import create_random_papel_valido

def test_list_papeis_vazio(client: TestClient) -> None:
    response = client.get("/papeis")
    content = response.json()
    assert response.status_code == 200
    assert len(content) == 0


def test_cria_papel(client: TestClient) -> None:
    body = create_random_papel_valido()
    response = client.post("/papeis/", json=body)
    content = response.json()
    assert response.status_code == 200
    assert content["cnpj"] == body["cnpj"]

def test_cria_papeis(client: TestClient) -> None:
    quantidade = 10
    for i in range(quantidade):
        body = create_random_papel_valido()
        response = client.post("/papeis/", json=body)
        content = response.json()
        assert response.status_code == 200
        assert content["cnpj"] == body["cnpj"]
    response = client.get("/papeis")
    content = response.json()
    assert response.status_code == 200
    assert len(content) == quantidade