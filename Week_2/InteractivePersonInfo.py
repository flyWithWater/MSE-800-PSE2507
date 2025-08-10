# Create an interactive Python program that collects a user’s name, age, and address, 
# stores them in a list called personal_details, and prints each detail with labels.
# Then, ask the user to enter how many years to add to their current age, update the age in the list, 
# and display the updated information in a formatted sentence. 



class PersonalInfo:
    
    def __init__(self,name:str,age:int,address:str):
        self.name = name
        self.age = age
        self.address = address
    
    def updateAgeBasedOnInitial(self,years:int):
        self.age += years
        if self.age<0:
            self.age = 0
            
        return self.age
    

    def print(self):
        print(f"name:{self.name}, age:{self.age},address:{self.address}")
    


def main():
    personal_details = list()
    person1 = PersonalInfo("zhang",40,"29 browns bay auckland")
    personal_details.append(person1)

    person2 = PersonalInfo("zhou",20,"city of Auckland")
    personal_details.append(person2)

    for person in personal_details:
        person.print()

        ageCorrect = input("how many years do you want to correct your age? please input a number:\n")  
        ageNumber = int(ageCorrect)                               
        person.updateAgeBasedOnInitial(ageNumber)

        person.print()
    
        print("\n\n")


if __name__ == "__main__":
    main()

