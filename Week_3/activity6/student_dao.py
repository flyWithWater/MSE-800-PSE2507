from sqlalchemy.orm import sessionmaker
from college_info_database import CollegeInfoDatabase
from all_entities import Student

class StudentDAO:
    def __init__(self):
        self.engine = CollegeInfoDatabase.init_engine()
        Session = sessionmaker(bind=self.engine,future=True)
        self.session = Session()

    def add(self, stu):
        self.session.add(stu)
        self.session.commit()

    def view_all(self):
        return self.session.query(Student).all()
    
    def view_by_id(self,id):
        return self.session.get(Student,id)

    def delete(self, stu):
        self.session.delete(stu)
        self.session.commit()


def test():
    # 创建表（确保先建表）
    CollegeInfoDatabase.create_table()

    dao = StudentDAO()

    # 插入学生对象，id 自动生成
    stu = Student(id=222,name="zcs", gender="male", nationality="china",
                  address="29 Kiteroa rothesay bay", phone_number="222")
    dao.add(stu)

    # 查看所有学生
    student_list = dao.view_all()
    print(f"All students: {student_list}")

    # 删除第一个学生
    if student_list:
        dao.delete(student_list[0])
        print("Deleted the first student.")

    print(f"Students after deletion: {dao.view_all()}")


if __name__ == "__main__":
    test()
