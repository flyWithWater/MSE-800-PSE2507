


import sqlite3

from sqlalchemy import create_engine
from sqlalchemy.orm import registry

mapper_registry = registry()

class ExpensesDatabase:
    DB_NAME = "expenses.db"
    DB_URL = "sqlite:///"+DB_NAME

     # create the connection with the Database
    @staticmethod
    def create_connection():
        connection = sqlite3.connect(ExpensesDatabase.DB_NAME)
        return connection
    
    @staticmethod
    def init_engine():
        engine = create_engine(ExpensesDatabase.DB_URL,echo=False,future=True)
        return engine
    
    @staticmethod
    def create_table():
        engine = ExpensesDatabase.init_engine()
        mapper_registry.metadata.create_all(engine)
