import databases
import sqlalchemy
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///wwwwdb.sqlite')
TEST_DATABASE = (os.getenv('TEST_DATABASE', 'false') in ("yes", "true", "t", "1"))
database = databases.Database(DATABASE_URL, force_rollback=TEST_DATABASE)
metadata = sqlalchemy.MetaData()
