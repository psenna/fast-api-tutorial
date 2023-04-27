from fastapi.testclient import TestClient
from models.cotacao import Cotacao
from models.papel import Papel
from tests.utils.papeis import create_papel_invalido, create_papel_valido
from tests.utils.cotacoes import create_cotacao_valida
import asyncio
import pytest
import ormar

def test_lista_todas_as_cotacoes(client: TestClient) -> None:
    atributos = create_papel_valido()
    papel = Papel(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(papel.save())

    atributos_cotacao = create_cotacao_valida(papel.id)
    cotacao = Cotacao(**atributos_cotacao)
    loop.run_until_complete(cotacao.save())
    
    response = client.get("/cotacoes/")
    content = response.json()

    assert response.status_code == 200
    assert len(content) == 1

def test_cria_cotacao(client: TestClient) -> None:
    atributos = create_papel_valido()
    papel = Papel(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(papel.save())
    
    body = create_cotacao_valida(papel.id)

    response = client.post("/cotacoes/", json=body)
    
    content = response.json()
    assert response.status_code == 200
    assert content["valor"] == body["valor"]

def test_cria_cotacao_com_valor_negativo(client: TestClient) -> None:
    atributos = create_papel_valido()
    papel = Papel(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(papel.save())
    
    body = create_cotacao_valida(papel.id)
    body['valor'] = -1
    
    response = client.post("/cotacoes/", json=body)
    content = response.json()
    assert response.status_code == 422

def test_obtem_uma_cotacao_por_id(client: TestClient) -> None:
    atributos = create_papel_valido()
    papel = Papel(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(papel.save())

    atributos_cotacao = create_cotacao_valida(papel.id)
    cotacao = Cotacao(**atributos_cotacao)
    loop.run_until_complete(cotacao.save())

    response = client.get(f"/cotacoes/{cotacao.id}")
    content = response.json()

    assert response.status_code == 200
    assert content["valor"] == cotacao.valor
    assert content["papel"]["sigla"] == papel.sigla

def test_obtem_uma_cotacao_inexistente_por_id(client: TestClient) -> None:
    response = client.get(f"/cotacoes/1")
    content = response.json()

    assert response.status_code == 404
    assert content["detail"] == "Entidade não encontrada"

def test_delete_papel_existente(client: TestClient) -> None:
    atributos = create_papel_valido()
    papel = Papel(**atributos)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(papel.save())

    atributos_cotacao = create_cotacao_valida(papel.id)
    cotacao = Cotacao(**atributos_cotacao)
    loop.run_until_complete(cotacao.save())

    response = client.delete(f"/cotacoes/{cotacao.id}")

    with pytest.raises(ormar.exceptions.NoMatch): 
        loop.run_until_complete(Cotacao.objects.get(id=cotacao.id))

    assert response.status_code == 200


def test_delete_cotacao_inexistente(client: TestClient) -> None:
    response = client.delete("/cotacoes/1")
    content = response.json()

    assert response.status_code == 404
    assert content["detail"] == "Entidade não encontrada"