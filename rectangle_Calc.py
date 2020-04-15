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
        for i in range(1, self.width+1):
            for j in range(1, self.height+1):
                if(i == 1 or i == self.height or
                  j == 1 or j == self.width):                    
                    output += "*"
                    print("*", end = " ")
                else:
                    print(" ", end=" ")
            print()
        return output




def main():
    print ("Rectangle Calculator\n")
    while True:
        a = int(input("Height: "))
        b = int(input("Width: "))
        obj = Rectangle(a,b)
        print("Area: ", obj.getArea())
        print("Peremeter: ", obj.getPeremeter())
        print()
        obj.printRectangle()
        choice = input("\nContinue? (y/n): ")
        if choice != "y":
            print ("\nBye!")
            break
if __name__ == "__main__":
    main()