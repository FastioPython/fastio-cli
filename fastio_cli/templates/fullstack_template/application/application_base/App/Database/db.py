from orator import DatabaseManager, Schema, Model
from App.Config.db import DATABASES

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)