# You are tasked with developing a simple program for the Human Resources (HR) department to store 
# and display basic employee information, including each employee’s name, salary, and job title.
# Requirements:
# Create at least two Employee objects with different data.
# Call the display_info() method to show each employee’s details.
# Call the give_raise() method to increase an employee’s salary and display the updated amount.
 
import numpy as np

class HumanInfo:
    def __init__(self,name:str,salary:float,title:str):
        self.name = name
        self.salary = salary
        self.title = title


    def display(self):
        print(f"name:{self.name}, title:{self.title},salary:{self.salary}\n")

    def raiseOrNot(self):
        commandStr = input("raise this employee or not? input Y or N to represent yes or no\n")
        if commandStr == "Y":
            self.give_raise()
        else:
            return

    def give_raise(self):
        raiseStr = input("how much do you wanna raise this employee's salary?\n")
        raiseNumber = int(raiseStr)
        self.salary += raiseNumber

        self.display()

        



class HumanResource:

    def __init__(self):
        self.allEmployees = list()
        self.allEmployees.append(HumanInfo("zhou",2000,"CEO"))
        self.allEmployees.append(HumanInfo("wu",1500,"CTO"))
    
    
    def interactive(self):
        for human in self.allEmployees:
            human.display()
            human.raiseOrNot()

    def display_info(self):
        print("=========================")
        for h in self.allEmployees:
            h.display()
        print("=========================")


def main():
    humanResource = HumanResource()
    humanResource.interactive()
    humanResource.display_info()



if __name__ == "__main__":
    main()


