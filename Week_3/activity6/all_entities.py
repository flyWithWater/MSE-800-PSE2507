from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from college_info_database import mapper_registry   

@mapper_registry.mapped
class Student:
    __tablename__ = "students"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(30))
    gender: str = Column(String(10))
    nationality: str = Column(String(30))
    address: str = Column(String(150))
    phone_number: str = Column(String(20))

    def __repr__(self):
       return f"<Student(id={self.id}, name='{self.name}', gender='{self.gender}',nationality='{self.nationality}')>"


    

class Clazz:
    id:int 
    name:str 
    student_representative:str 
    classroom:str  


@mapper_registry.mapped
class Lecturer:
    __tablename__ = "lecturers"

    id:int= Column(Integer,primary_key=True,autoincrement=True)
    name:str =Column(String(30))
    gender:str=Column(String(20))
    phone_number:str=Column(String(30))
    email:str =Column(String(50))

    def __repr__(self):
       return f"<Lecturer(id={self.id}, name='{self.name}', gender='{self.gender},email='{self.email}'')>"

@dataclass
class course:
    id:int
    name:str
    credit:int
    
@dataclass
class student_lecturer_relation:
    student_id:int
    lecturer_id:int

@dataclass
class teching_info:
    lecturer_id:int
    class_id:int

@dataclass
class clazz_course_relation:
    class_id:int
    course_id:int