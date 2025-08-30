
# Add one more method to the class that uses the private attribute. Also, please create a new class 
# to demonstrate the use of the public and protected attributes. See attached file- See slide 3 : 
# Note: Include a comment in the code that explains your understanding of encapsulation.


class Student:

    def __init__(self, name, age, gender):
        self.name = name # public​
        self._age = age # protected​
        self.__grade = 'A' # private​
        self.__gender = gender #private


    def get_grade(self):
        return self.__grade
    

    def get__gender(self):
        return self.__gender
    

#encapsulation is just a method to control the access of the information(attribute) and the call of our methods
#also, it also can make our software or sdk be more secure when we supply it to others.
class PrimarySchoolStudent:


    def __init__(self, name, age,grade, gender):
        self.name = name #public attribute
        self.__age = age #private attribute
        self.__grade = grade #private attribute
        self.__gender = gender #private attribute
    

    def get_age(self):
        return self.__age
    
    def get_grade(self):
        return self.__grade
    



def main():
    s = Student('Ali', 20,"female")
    print(s.name) # accessible​
    print(s._age) # discouraged​
    print(s.get_grade()) # correct way

    pss = PrimarySchoolStudent("zhang",10,100,"male")
    print(pss.name)
    print(pss.get_grade)


if __name__=="__main__":
    main()