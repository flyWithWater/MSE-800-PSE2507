from sqlalchemy.orm import sessionmaker
from college_info_database import CollegeInfoDatabase
from all_entities import Lecturer

class LecturerDao:
    def __init__(self):
        self.engine = CollegeInfoDatabase.init_engine()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add(self, lec):
        self.session.add(lec)
        self.session.commit()

    def view_all(self):
        return self.session.query(Lecturer).all()
    
    def view_by_id(self,id):
        return self.session.get(Lecturer,id)

    def delete(self, lec):
        self.session.delete(lec)
        self.session.commit()
