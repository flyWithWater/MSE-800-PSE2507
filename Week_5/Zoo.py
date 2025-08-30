



class Color:
    name:str
    def __init__(self,name):
        self.name = name 

    def show_color(self):
        print(f"{self.name}")
        


class TransparentColor(Color):

    def __init__(self,name):
        super().__init__(name)


    def show_color(self):
        print(f"transparent")



def main():
    red = Color("red")
    transparent = TransparentColor("black")

    red.show_color()
    transparent.show_color()





if __name__ == "__main__":
    main()