from tests.utils.papeis import create_papel_valido, create_papel_invalido
from models.papel import Papel
import pytest

def test_cria_papel_valido() -> None:
    atributos = create_papel_valido()
    papel = Papel(**atributos)

def test_cria_papel_com_sigla_invalida() -> None:
    with pytest.raises(ValueError, match='A sigla do papel é inválida!'):
        atributos = create_papel_invalido(['sigla'])
        papel = Papel(**atributos)