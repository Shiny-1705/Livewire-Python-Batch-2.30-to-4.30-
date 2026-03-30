#Q1: Exception Handling
'''
Write a program:
Take input from user
Convert to int
Print 100 / num
Handle:
ValueError
ZeroDivisionError

#Answer
try:
    num=input("Enter your String:")
    n=int(num)
    result=100/n
    print(result)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Cannot divide by zero")
'''
#Q2: File Handling
'''
Write a program:
Write "Welcome to Python" into file
Read and print it

#Answer
with open("text.txt","w") as f:
    f.write("Welcome to Python")
with open("text.txt","r") as f:
    print(f.read())
'''
#Q3: Class & Object
'''
Create class Car:
Attribute: brand
Create 2 objects
Print both brands

#Answer
class Car():
    brand=""
c1=Car()
c2=Car()
c1.brand="RollsRoyce"
c2.brand="BMW"
print(c1.brand)
print(c2.brand)
''' 
#Q4: Constructor
'''
Create class Student:
Constructor takes name and age
Print both using object

#Answer
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Student("Tamil",21)
print(s1.name)
print(s1.age)
'''
#Q5: Single Inheritance
'''
Create:
Class Person → method show()
Class Student(Person)
Call method using student object

#Answer
class Person:
    def show(self):
        print("Person")
class Student(Person):
    pass
s=Student()
s.show()
'''
#Q6: Multilevel Inheritance
'''
Create:
Class A → method display()
Class B(A)
Class C(B)
Call method using C

#Answer
class A:
    def display(self):
        print("A")
class B(A):
    pass
class C(B):
    pass
c=C()
c.display()
'''
#Q7: Multiple Inheritance
'''
Create:
Class A → method methodA()
Class B → method methodB()
Class C(A, B)
Call both methods

#Answer
class A:
    def methodA(self):
        print("A")
class B:
    def methodB(self):
        print("B")
class C(A,B):
    pass
c=C()
c.methodA()
c.methodB()
'''
#Q8: Method Overriding
'''
Create:
Class Animal → method sound()
Class Dog(Animal) → override → "Dog barks"

#Answer
class Animal():
    def sound(self):
        print("Animal makes Sound")
class Dog(Animal):
    def sound(self):
        print("Dog Barks")
d=Dog()
d.sound()
'''
#Q9: Encapsulation
'''
Create:
Private variable __salary
Create method to access it

#Answer
class Person:
    def __init__(self):
        self.__salary=50000
    def get_salary(self):
        return self.__salary
p=Person()
print(p.get_salary())
'''
#Q10: Abstraction
'''
Use abc module:
Create abstract class Shape
Abstract method area()
Create class Square → implement area

#Answer
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def area(self):
        print("Area of Square")
s=Square()
s.area()
'''     
#Q11:
'''
Combine:
File handling + Exception

#Answer
try:
    with open("data.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("No file found")
'''
#Q12:
'''
Operator overloading example (just demonstrate with +)

#Answer
a=7
b=10
print(a+b)
c="King"
d=" Tamil"
print(c+d)
'''












































