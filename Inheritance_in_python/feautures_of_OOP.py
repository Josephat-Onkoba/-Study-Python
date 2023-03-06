#Encapsulation - containing information in an object, exposing only selected information
# 2. Inheritance
  # SYNTAX
'''
#Parent class 
class A:
    pass
#child class
class B(A): - inherits some attributes of class A
  pass'''
#types of inheritance
'''
i) single inheritance 
class A:
    pass:
class B(A):
    pass
    
    #example 1

class Animal:
    def legs(self):
        print("I have four legs")
    def fur(self):
        print("My body is covered with fur")
class Dog(Animal):
    def bark(self):
        print("The dogs barks")
    def run(self):
        print("I run as fast as a horse")
class Eat(Dog):
    def carnivore(self):
        print("I am a Carnivorous animal")
d = Eat()
d.bark()
d.legs()
d.fur()
d.run()
d.carnivore()

ii)
multiple inheritance
class A:
    pass:
class B:
    pass:
class C(A,B):
pass

iii)multi level inheritance
class A:
    pass:
class B(A):
 pass
class C(B)
pass

    #Example 2
class Classroom:
    def desk(self):
        print("Desk")
    def student(self):
        print("Student")

class Sports:
    def football(self):
        print("Students partcipate in playing football")
class clubs:
    def ITECH(self):
        print("Most students are part of ITECH Club")
class School(Classroom,Sports,clubs):
    def institution(self):
        print("An institution contains all of these: ")
   
You = School()
You. institution()
You.desk()
You.student()
You.football()
You.ITECH()

iv)Hierarchichal inheritance
class A:
    pass
class B(A)
    pass
class C(A):
pass

v) Hybrid inheritance
'''



# 3. Polymorphism
# 4 . Abstraction

#Exercise (PAYROLL SYSTEM)