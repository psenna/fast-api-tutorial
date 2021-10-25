from fastapi.testclient import TestClient

def get_root(
    client: TestClient
) -> None:
    response = client.get("/")
    content = response.json()
    assert response.status_code == 200
    assert content["mensagem"] == "Api de papeis"
