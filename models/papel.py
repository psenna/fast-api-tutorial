import ormar
from sqlalchemy.sql.expression import table
from config import database, metadata

class Papel(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "papeis"

    id: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(max_length=100)
    sigla: str = ormar.String(max_length=10)
    cnpj: str = ormar.String(max_length=20)