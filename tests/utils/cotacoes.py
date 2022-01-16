from datetime import datetime

def create_cotacao_valida(papel):
    return {
        "id": 0,
        "valor": 25,
        "horario": str(datetime.now()),
        "papel": papel,
    }