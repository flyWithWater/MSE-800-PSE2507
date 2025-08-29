
from datetime import date

#basic class or superclass
class Person:
    def __init__(self,name:str,birthDay:date,address:str):
        self.name = name
        self.birthDay = birthDay
        self.address = address

    def greeting(self):
        print("Hi, how are you?   from Person")

    def printSelf(self):
        print(f"name:{self.name},birthday:{self.birthDay}")


#subclass of the class Person
class Student(Person):
    def __init__(self, name, birthDay, address,academic_score:int):
        super().__init__(name, birthDay, address)
        self.academic_score = academic_score


#subclass of the class Person
class Staff(Person):
    def __init__(self, name, birthDay, address,tax_code:str, salary:int):
        super().__init__(name, birthDay, address)
        self.tax_code = tax_code
        self.salary = salary
    
    #overrid the method inherited from the class Person
    def printSelf(self):
        print(f"name:{self.name},birthday:{self.birthDay},salary:{self.salary}")

    #override the method inherited from the class Person
    def greeting(self,who="student"):

        print(f"[from Staff] Hello, Our dear ",end="")
        if who=="student":
            print("classmate")
        elif who == "staff":
            print("colleague")

class Academics(Staff):
    def __init__(self, name, birthDay, address, tax_code, salary,lecturer_level:str):
        super().__init__(name, birthDay, address, tax_code, salary)
        self.lecturer_level = lecturer_level



def main():
    person = Person("zhang",date(1999,8,11),"auckland")
    person.greeting()
    staff = Staff("zzzz",date(1980,8,14),"city,Auckland","234234242",10000)
    staff.greeting()



if __name__ == "__main__":
    main()