

from datetime import datetime
from git import AmbiguousObjectName
from numpy import integer
from sqlalchemy import Column, Integer,String,Boolean,DateTime
from dao.expense_db import mapper_registry

@mapper_registry.mapped
class ExpenseItem:
    __tablename__ = "expenses"

    id:int = Column(Integer,primary_key=True,autoincrement=True)
    amount:int = Column(Integer)
    expense_name:str = Column(String(50))
    create_time:datetime = Column(DateTime(),default= datetime.utcnow())




