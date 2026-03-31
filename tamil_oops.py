#Class and Object
'''
#Create a class Student with name and marks and display the values using an object
class Student():
    name="Tamil"
    mark=90
s=Student()
print(s.name)
print(s.mark)

#Create a class with a method and call it using an object
class Student():
    def show(self):
        print("Tamil")
s=Student()
s.show()

#Create multiple objects for a class and display different values
class Person():
    def __init__(self,name):
        self.name=name
p1=Person("Father")
p2=Person("Son")
print(p1.name)
print(p2.name)
'''
#Inheritance
'''
#Write a program to demonstrate Single Inheritance
class Father():
    def show(self):
        print("Father")
class Son(Father):
    pass
s=Son()
s.show()

#Write a program to demonstrate Multiple Inheritance
class Father():
    def show1(self):
        print("Father")
class Mother():
    def show2(self):
        print("Mother")
class Son(Father,Mother):
    pass
s=Son()
s.show1()
s.show2()

#Write a program to demonstrate Multilevel Inheritance
class Father():
    def show(self):
        print("Father")
class Mother(Father):
    pass
class Son(Mother):
    pass
s=Son()
s.show()

#Write a program to demonstrate Hierarchical Inheritance
class Father():
    def show(self):
        print("Father")
class Mother(Father):
    pass
class Son(Father):
    pass
s=Son()
s.show()

#Write a program to demonstrate Hybrid Inheritance
class Father():
    def show(self):
        print("Father")
class Mother(Father):
    pass
class Son(Father):
    pass
class Daughter(Mother,Son):
    pass
d=Daughter()
d.show()
'''
#Abstraction
'''
#Create an abstract class and implement it using a child class
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog barks")
d=Dog()
d.sound()

#Create an abstract method and override it in the child class
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
c=Cat()
c.sound()
'''
#Encapsulation (Public, Private, Protected)
'''
#Create a class with public variable and access it
class Student():
    def __init__(self):
        self.name="Tamil"
s=Student()
print(s.name)

#Create a class with protected variable and access it
class Student():
    def __init__(self):
        self._name="Tamil"
s=Student()
print(s._name)

#Create a class with private variable and access it using a method
class Student():
    def __init__(self):
        self.__name="Tamil"
    def get_name(self):
        return self.__name
s=Student()
print(s.get_name())

#Write a program using getter and setter methods
'''
#Polymorphism
'''
#Create two classes with same method name and show polymorphism
#Method Overriding
class Parent():
    def show(self):
        print("Parent")
class Child(Parent):
    def show(self):
        print("Child")
c=Child()
c.show()

#Method Overloading
def add(a,b,c=0):
    return a+b+c
print(add(2,3))
print(add(2,3,5))

#Write a program for operator overloading using +
a=10
b=15
print(a+b)
str1="King"
str2=" Tamil"
print(str1+str2)
'''














