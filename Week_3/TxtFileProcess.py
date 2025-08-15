



class TxtFileHandler:
    
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        
        file_handle = open(self.file_name)
        print("Now I am going to print your file:")
        lines = file_handle.readlines()

        for line in lines:
            print(line[0:-1])

        file_handle.close


    def write(self):
        file_handle = open(self.file_name, "w")
        print("Write the following text to the file you just opened...")
        string = input("please input text to write in the file\n ")
        file_handle.write(string)
        file_handle.close()













def main():
    myfile = TxtFileHandler("/Users/zcs/github/MSE-800-PSE2507/Week_3/demo_file.txt")
    myfile.read()  

    myfile.write()
  


if __name__ == "__main__":
    main()