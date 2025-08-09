import random as rd

class GuessWord:

    initial_life_cycles:int = 10
    word_need_to_guess:str = ""
    word_guess_situation:str = '_'

    def __init__(self):
        wordsArray = ["happy","random","five","sad","excellent"]

        global word_need_to_guess
        global word_guess_situation
        
        self.word_need_to_guess = rd.choice(wordsArray)

        for i in range(1,len(self.word_need_to_guess)):
            self.word_guess_situation = (self.word_guess_situation+" "+"_")
        

 
        
            

        



    def printCurrentStatus(self):
        global initial_life_cycles
        global word_need_to_guess
        global word_guess_situation

        print(f"Remaining life cycle is {self.initial_life_cycles}\n")
        print(f"Now the words is :{self.word_guess_situation}")

    def isGameOver(self)-> bool:
        global initial_life_cycles
        global word_need_to_guess
        global word_guess_situation
    
        return (self.initial_life_cycles<=0) | ('_' in self.word_guess_situation)

    def guess(self):
        #global initial_life_cycles
        global word_need_to_guess
        global word_guess_situation

        print(self.word_guess_situation)
        letter:str = input("Please input a letter to guess the word step by step\n");
        if(len(letter)!=1):
            print("error! you need to input a letter each time!")
            return;

        if(letter in self.word_need_to_guess):
            index = self.word_need_to_guess.find(letter)
            indexInProcessStr:int = 0

            if(index>0):
                indexInProcessStr = index*2
            charsOfProcessStr = list(self.word_guess_situation)

            charsOfProcessStr[indexInProcessStr] = letter
            self.word_guess_situation = "".join(charsOfProcessStr)
            
        else:   
            self.initial_life_cycles -=1
            print("Come on! Keep going!")

            
        



    def play(self):
        #generate random words
        while(self.isGameOver()):
            self.guess()
            print("-------------------------------\n")
        
            self.printCurrentStatus()
        print("Game over!") 

if __name__ == "__main__":
    gw = GuessWord()
    gw.play()