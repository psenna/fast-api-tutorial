import os
DATABASE_URL = 'sqlite:///testedb.sqlite'
os.environ['DATABASE_URL'] = DATABASE_URL
os.environ['TEST_DATABASE'] = 'true'

from typing import Generator
from fastapi.testclient import TestClient
import pytest
from main import app
from cria_tabelas import configurar_banco 

@pytest.fixture(scope="function")
def client() -> Generator:
    configurar_banco(DATABASE_URL)
    with TestClient(app) as c:
        yield c