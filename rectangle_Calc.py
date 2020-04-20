#!/usr/bin/env python3 

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def getPeremeter (self):
        return (self.width * 2) + (self.height * 2)

    def getArea (self):
        return self.width * self.height
    
    def printRectangle (self):
        output = ""
        for row in range(0, self.height):
            for column in range(0, self.width):
                if (row == 0 or row == self.height - 1 or column == 0 or column == self.width - 1):
                    output += "* "
                else:
                    output += "  "
            output += "\n"
        return output

class Square(Rectangle):
    def __init__(self, width, height):
       
        super(Square, self).__init__(width, height)
        

def main():
    print("--RECTANGLE CALCULATOR--")
    choice1 = 'y'
    while choice1.lower() == 'y':
        while True:
            choice2 = str(input("Rectangle or Square? (s/r): "))
            if choice2.lower() == 's':
                print ("Im a Square!!")
                a = int(input("Length: "))
                obj = Square(a,a)
                print("Area: ", obj.getArea())
                print("Peremeter: ", obj.getPeremeter())
                print()
                print(obj.printRectangle())
                break
            if choice2.lower() == 'r':
                print ("Im a Rectangle")
                a = int(input("Height: "))
                b = int(input("Width: "))
                obj = Rectangle(a,b)
                print("Area: ", obj.getArea())
                print("Peremeter: ", obj.getPeremeter())
                print()
                print(obj.printRectangle())
                break
            else:
                print ("Please Make a Proper Selection")
                continue
        choice1 = str(input("Would you like to continue? (y/n): "))
        if choice1.lower() != 'y':
            print("BYE!!!!")
            break


if __name__ == "__main__":
    main()

