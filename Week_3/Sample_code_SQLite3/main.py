from database import create_table
from user_manager import add_user, view_users, search_user, delete_user
from student_manager import *


def show_all_data():
    users = view_users()   
    print("All users are :----")
    for user in users:
        print(user)
    print("-----------")
    students = StudentManager.view_all_students()
    print("All students are :-------")
    for student in students:
        print(student)
    print("---------------")

def insert_two_students():
    StudentManager.add_student('Ravi', 'Rampura')
    StudentManager.add_student('Sonu', 'Shahpur')
    print("\nInserted 2 Students")

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. insert two students automatically")
    print("6. show all the students and users together")
    print("7. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-5): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            insert_two_students()    
        elif choice == '6':
             show_all_data()
        elif choice == '7':
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
