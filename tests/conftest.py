import os
DATABASE_URL = 'sqlite:///testdb.sqlite'
os.environ["DATABASE_URL"] = DATABASE_URL
os.environ["TEST_DATABASE"] = 'true'

from typing import Generator
from fastapi.testclient import TestClient
import pytest
from main import app
from cria_tabelas import configura_banco 

@pytest.fixture(scope="function")
def client() -> Generator: 
    configura_banco(DATABASE_URL)
    with TestClient(app) as c:
        yield c