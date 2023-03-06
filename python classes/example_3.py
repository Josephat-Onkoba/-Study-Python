# Create a class named Rectangle. Initialize it with lenght and width.
#Make two methods to return the area and perimeter

class Rectangle:
    def __init__(self,lenght,width):
        self.lenght = lenght
        self.width = width
    
    def area(self):
        return self.lenght*self.width
    
    def perimeter(self):
        return 2*(self.width + self.lenght)
    
A = Rectangle(lenght = float(input("Enter Lenght : ")),
               width = float(input("Enter width : ")))
print(A.area())
print(A.perimeter())