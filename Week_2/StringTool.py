


class StringTool:

    def __init__(self,initalStr):
        self.initialStr = initalStr
        pass

    def findCharacter(self,character) -> int:
        return self.initialStr.find(character)
        

    def length(self)->int:
        return len(self.initialStr)
    

    def upperConvert(self)->str:
        return self.initialStr.upper()
    


str = StringTool("abcdefg")
print(f"the position of the charactor is : {str.findCharacter('c')}")
print(f"the length of it is {str.length()}")
print(f"the upper format of it is {str.upperConvert()}")