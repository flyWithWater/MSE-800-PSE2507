import argparse

print("------------test-----------")

def printFactorial():
    numStr = input("Please input a number equal or grater than 0:")
    
    

    num = int(numStr)
    

    if(num<0):
        print("Error! It is illegal to caculate a negative number's factorial.")
        return
    if(num==0 or num==1):
        print("resut is 1")
        return
    
    result = 1
    for i in range(1,num+1):
        result *= i
    
    print(f"resut is {result}")

    

printFactorial()


