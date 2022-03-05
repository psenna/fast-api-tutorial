import email
from models.usuario import Usuario
from tests.factory.usuario_factory import UsuarioFactory
from models.papel import Papel
import pytest

def test_cria_usuario_valido() -> None:
    atributos = UsuarioFactory.get_prorpiedades_validas()
    usuario = Usuario(**atributos)

def test_cria_usuario_com_email_invalido() -> None:
    atributos = UsuarioFactory.get_prorpiedades_validas()
    with pytest.raises(ValueError, match='O formato do email é inválido!'):
        atributos = UsuarioFactory.get_prorpiedades_validas({'email': "emailerrado"})
        usuario = Usuario(**atributos)

def test_adiciona_funcao_usuario() -> None:
    atributos = UsuarioFactory.get_prorpiedades_validas()
    usuario = Usuario(**atributos)
    usuario.funcoes += ["admin"]
    assert "admin" in usuario.funcoes

def test_adiciona_varias_funcoes_usuario() -> None:
    atributos = UsuarioFactory.get_prorpiedades_validas()
    usuario = Usuario(**atributos)
    novas_funcoes = ["admin", "operador"]
    usuario.funcoes += novas_funcoes
    for funcao in novas_funcoes:
        assert funcao in usuario.funcoes

def test_adiciona_funcao_duplicada_usuario() -> None:
    atributos = UsuarioFactory.get_prorpiedades_validas()
    usuario = Usuario(**atributos)
    usuario.funcoes += ["admin"]
    assert "admin" in usuario.funcoes
    usuario.funcoes += ["admin"]
    assert "admin" in usuario.funcoes
    assert len(usuario.funcoes) == 1


def test_adiciona_funcao_inexiustente_usuario() -> None:
    with pytest.raises(ValueError, match='A função gerias não é um função válida!'):
        atributos = UsuarioFactory.get_prorpiedades_validas()
        usuario = Usuario(**atributos)
        usuario.funcoes += ["gerias"]
