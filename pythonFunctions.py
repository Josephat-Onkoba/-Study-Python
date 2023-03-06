#A function is a block of code which only runs when it is called
#Types of Functions
# 1. User defined functions
# 2. Built-in Functions e.g print(), lower(), pow()
# 3. Lambda functions - are anonymous un-named functions
# 4. Recursion functions - calls itself
# A function is defined using the *def* keyword

# 1st Example of function to calculate Area of circle

'''from math import pi


def Area_of_Circle(r):
    area = pi * r * r
    print ("Area of Circle : ", area)
r = float(input("Enter radius : "))
Area_of_Circle(r)'''

# 2nd Example of function to calculate Volume of a cylinder

'''from math import pi

def volume_of_a_Cylinder(radius, height):
    volume = pi * radius * radius * height
    print("Volume of a Cylinder = ", volume)
volume_of_a_Cylinder(10,20)'''

# 3rd Example of function to calculate Volume of a sphere
'''from math import pi

def volume_of_a_Sphere(radius):
    volume = (4/3) * pi * radius * radius * radius
    print("Volume of a Sphere = ",volume)
volume_of_a_Sphere(10)'''

# 4th Example of function to calculate area of a rectangle

'''def area_of_a_Rectangle(L,W):
    area = L * W
    print("Area of a rectangle = ", area)
area_of_a_Rectangle(10,20)'''

#5th Example of function to calculate compound interest
def Compound_interest(principal,rate,time):
    Amount = principal * ( pow((1 + rate/100 ), time))
    CompoundInterest = Amount - principal
    print("Compound Interest is : ", CompoundInterest)
principal = int(input("Enter the principal Amount : "))
rate = int(input("Enter rate of interest : "))
time = int(input("Enter Time in years : "))
Compound_interest(principal,rate,time)