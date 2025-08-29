
from datetime import date


class Person:
    def __init__(self,name:str,birthDay:date,address:str):
        self.name = name
        self.birthDay = birthDay
        self.address = address



class Student(Person):
    def __init__(self, name, birthDay, address,academic_score:int):
        super().__init__(name, birthDay, address)
        self.academic_score = academic_score


class Staff(Person):
    def __init__(self, name, birthDay, address,tax_code:str, salary:int):
        super().__init__(name, birthDay, address)
        self.tax_code = tax_code
        self.salary = salary
    
    def printSelf(self):
        print(f"name:{self.name},birthday:{self.birthDay},salary:{self.salary}")


class Academics(Staff):
    def __init__(self, name, birthDay, address, tax_code, salary,lecturer_level:str):
        super().__init__(name, birthDay, address, tax_code, salary)
        self.lecturer_level = lecturer_level



def main():
    staff = Staff("zzzz",date(1980,8,14),"city,Auckland","234234242",10000)
    staff.printSelf()


if __name__ == "__main__":
    main()