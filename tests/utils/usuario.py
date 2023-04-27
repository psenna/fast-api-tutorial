from security import get_password_hash

def create_usuario_valido():
    return {
        "id": 0,
        "nome": "usuario",
        "email": "mail@mail.com",
        "hash_password": get_password_hash("senha"),
    }

def create_requisicao_usuario_valida():
    return {
        "id": 0,
        "nome": "usuario",
        "email": "mail@mail.com",
        "password": "senha",
    }
