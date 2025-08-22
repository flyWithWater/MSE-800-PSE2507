from class_dao import ClassDao
from lecturer_dao import LecturerDao
from student_dao import StudentDAO
from all_entities import Clazz
from all_entities import Student
from all_entities import Lecturer
from college_info_database import CollegeInfoDatabase

class Menu:

    @staticmethod
    def main_menu():
        print('''
               Main menu:
                     input 1: enter class menu;
                     input 2: enter lecturer menu;
                     input 3: enter student menu;
                     input 4: exit;
        
        ''')

    @staticmethod
    def main_menu_loop():
        CollegeInfoDatabase.create_table()

        while True:
            Menu.main_menu()
            choose = input(" please input a menu number:")

            if choose=='1':
                print("You chose class menu!")
                Menu.class_menu()
            
            elif choose == '2':
                print("You chose lecturer menu!")
                Menu.lecturer_menu()

            elif choose == '3':
                print("You chose student menu!")
                Menu.student_menu()
            
            elif choose =='4':
                print("You chose exit!")
                break


    @staticmethod
    def class_menu():
        dao = ClassDao()

        while True:
            print('''
                Class menu:
                        input 1: add a class;
                        input 2: view all classes;
                        input 3: delte a class;
                        input 4: exit;
            
            ''')
            choice = input("Please input your choice:")
            if   choice == '1':
                Menu.add_class(dao) 
            elif choice =='2':
                clzz_list = dao.viewAll()
                print("-----------")    
                for clzz in clzz_list :
                    print(clzz)
                print("-----------")    
            elif choice =='3':
                clzz_id = input("please input the id of the class you want to delete:")
                dao.delete(clzz_id)
                print(f"id:{id} already been deleted.")
            elif choice =='4':
                break

    
    @staticmethod
    def student_menu():
        dao = StudentDAO()

        while True:
            print('''
                Class menu:
                        input 1: add a student;
                        input 2: view all student;
                        input 3: delte a student;
                        input 4: exit;
            
            ''')
            choice = input("Please input your choice:")
            if   choice == '1':
                Menu.add_student(dao) 
            elif choice =='2':
                stu_list = dao.view_all()
                print("-----------")    
                for stu in stu_list :
                    print(stu)
                print("-----------")    
            elif choice =='3':
                stu_id = input("please input the id of the student you want to delete:")
                stu = dao.view_by_id(stu_id)
                dao.delete(stu)
                print(f"id:{id} already been deleted.")
            elif choice =='4':
                break


    
    @staticmethod
    def lecturer_menu():
        dao = LecturerDao()
        

        while True:
            print('''
                Class menu:
                        input 1: add a lecturer;
                        input 2: view all lecturer;
                        input 3: delte a lecturer;
                        input 4: exit;
            
            ''')
            choice = input("Please input your choice:")
            if   choice == '1':
                Menu.add_lecturer(dao) 
            elif choice =='2':
                lec_list = dao.view_all()
                print("-----------")    
                for lec in lec_list :
                    print(lec)
                print("-----------")    
            elif choice =='3':
                lec_id = input("please input the id of the lecturer you want to delete:")
                
                lec = dao.view_by_id(lec_id)
                if lec is None:
                    print(f"there is no student with id:{lec_id}")
                else:
                    dao.delete(lec)
                    print(f"id:{lec_id} have been deleted!")
                
                
            elif choice =='4':
                break

        





    @staticmethod
    def add_class(dao:ClassDao):
        
        name = input(" please input the name of the class:")
        student_representative = input("please input the student_representative of the class:")
        classroom = input("please input the classroom of the class:")

      
        dao.add(name,student_representative,classroom)
        print("---already successfully added the class.")

        
    @staticmethod
    def add_student(dao:StudentDAO):
        print("---start to add student--")
        
        name = input("please input the name of the student:")
        gender = input("please input the gender of the student:")
        nationality = input("please input the nationality of the student:")
        address = input("please input the address of the student:")
        phone_number = input("please input the phone_number of the student:")
        
        stu = Student(name=name,gender=gender,nationality=nationality,address=address,phone_number=phone_number)
        dao.add(stu=stu)
        print("---already successfully added the Student.")
    
    @staticmethod
    def add_lecturer(dao:LecturerDao):
        print("---start to add lecturer--")
        
        name = input("please input the name of the lecturer:")
        gender = input("please input the gender of the lecturer:")
        phone_number = input("please input the phone_number of the lecturer:")
        email = input("please input the email of the lecturer:")

        lec = Lecturer(name=name,gender=gender,phone_number=phone_number,email=email)

        dao.add(lec=lec)
        print("----add Lecturer successfully!")

    

    




if __name__ == "__main__":
    Menu.main_menu_loop()