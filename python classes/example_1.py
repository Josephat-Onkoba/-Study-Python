from pyclbr import Class


class Student:
 def __init__(self,name,percentage):
    self.name = name
    self.percentage = percentage
 def show(self):
    print("Name is ", self.name, "and percentage is : ", self.percentage)
stud = Student("Jessica",80)
stud.show()
# Class Attributes
# 1. Instance Variables
# 2 Class Variables
# What is an object - it is an instance of a class . It is also a collection of attributes(variables) of methods
# Types of constructors
# 1 Default
# 2.Non-parameterized
# 3. Parameterized
