


class StringTool:

    

    def findCharacter(self,strParameter:str,character) -> int:
        return strParameter.find(character)
        

    def length(self,strParameter:str)->int:
        return len(strParameter)
    

    def upperConvert(self,strParameter:str)->str:
        return strParameter.upper()
    


def main():
    strtool = StringTool()
    print(f"the position of the charactor is : {strtool.findCharacter("abcdefg",'c')}")
    print(f"the length of it is {strtool.length("abcdefg")}")
    print(f"the upper format of it is {strtool.upperConvert("abdcdddfdfdsafadsfadf")}")



if __name__ == "__main__":
    main()


