



class Color:
    name:str
    red:int
    green:int
    blue:int

    def __init__(self,name:str,red:int,green:int,blue:int):
        self.name = name 
        self.red = red
        self.blue = blue
        self.green = green


    def show_color(self):
        format = f"{self.name}, r:{self.red},g:{self.green},b:{self.blue}"
        print(format)
        return format
        


class TransparentColor(Color):
    transparent:int

    def __init__(self,name,red,green,blue,transparent:int):
        super().__init__(name,red,green,blue)
        self.transparent = transparent


    def show_color(self):
        normal_format = super().show_color()
        format = normal_format + f",transparent:{self.transparent}"
        print(format)
        return format






def main():
    red = Color("red",0xff,0x00,0x00)
    transparent = TransparentColor("transparent",0xff,0x00,0x00,199)

    red.show_color()
    transparent.show_color()





if __name__ == "__main__":
    main()