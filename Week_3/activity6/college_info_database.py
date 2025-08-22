import sqlite3

from sqlalchemy import create_engine
from sqlalchemy.orm import registry

# 统一全局 mapper_registry
mapper_registry = registry()

class CollegeInfoDatabase:
    DB_NAME = "yoobee_college_info.db"
    DB_URL = "sqlite:///"+DB_NAME

    @staticmethod
    def create_connection():
        connection = sqlite3.connect(CollegeInfoDatabase.DB_NAME)
        return connection
    

    @staticmethod
    def init_engine():
        # 创建统一 engine
        engine = create_engine(CollegeInfoDatabase.DB_URL, echo=True, future=True)
        return engine


    @staticmethod
    def create_table():
        # 使用统一的 engine 和 mapper_registry 创建表
        engine = CollegeInfoDatabase.init_engine()
        mapper_registry.metadata.create_all(engine)

        connection = CollegeInfoDatabase.create_connection()
        cursor = connection.cursor()
        cursor.execute('''
            create table if not exists class(
                 id integer primary key autoincrement,
                 name text not null,
                 student_representative_id int not null,
                 classroom text not null                  
                )
        ''')
        connection.commit()
        connection.close()
  

  
    
  
        