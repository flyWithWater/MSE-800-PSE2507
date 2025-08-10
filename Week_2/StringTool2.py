# Develop a project using class and methods to get a sentence from user input and find the number of words in it.

class StrTool2:

    def __init__(self):
        self.inputedText = input("please input a sentence: ")



    def search(self):
     
        array = self.inputedText.split(' ')

        return len(array)





def main():
    strtool2 = StrTool2()

    print(f"the Sentence you inputted just now has {strtool2.search()} words");


if __name__ == "__main__":
    main()

