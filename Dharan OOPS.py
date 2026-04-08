# class Student:
#     name="Dharani"
#     marks="95"
# print(Student.marks)
# print(Student.name)
#
# class Student:
#     def __init__(self, name, mark):
#         self.name = name
#         self.mark = mark
#     def display(self):
#         print("Name:", self.name)
#         print("Mark:", self.mark)
#         print("---------------")


# Single inheritance
# class Parent:
#     def display(self):
#         print("This is Parent class")
# class Child(Parent):
#     def show(self):
#         print("This is Child class")
# obj = Child()
# obj.display()
# obj.show()


# Multiple inheritance
# class Father:
#     def car1(self):
#         print("Father's car")
# class Mother:
#     def car2(self):
#         print("Mother's car")
# class Child(Father, Mother):
#     def car3(self):
#         print("Child's car")
# obj = Child()
# obj.car1()
# obj.car2()
# obj.car3()


# # Multilevel inheritance
# class Grandparent:
#     def show1(self):
#         print("Grandparent class")
# class Parent(Grandparent):
#     def show2(self):
#         print("Parent class")
# class Child(Parent):
#     def show3(self):
#         print("Child class")
# obj = Child()
# obj.show1()
# obj.show2()
# obj.show3()


#Hierarchical inheritance
# class Parent:
#     def display(self):
#         print("This is Parent class")
# class Child1(Parent):
#     def show1(self):
#         print("This is Child1")
# class Child2(Parent):
#     def show2(self):
#         print("This is Child2")
# obj1 = Child1()
# obj2 = Child2()
# obj1.display()
# obj1.show1()
# obj2.display()
# obj2.show2()


# Hybrid inheritance
# class Grandparent:
#     def show1(self):
#         print("Grandparent")
# class Parent1(Grandparent):
#     def show2(self):
#         print("Parent1")
# class Parent2(Grandparent):
#     def show3(self):
#         print("Parent2")
# class Child(Parent1, Parent2):
#     def show4(self):
#         print("Child")
# obj = Child()
# obj.show1()
# obj.show2()
# obj.show3()
# obj.show4()

#
# from abc import ABC, abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
# class Dog(Animal):
#
#     # Overriding Abstract Method
#     def sound(self):
#         print("Dog barks")
# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")
# d = Dog()
# c = Cat()
# d.sound()
# c.sound()

#
# class student:
#     name="Dharani"
#     _age=18
#     __marks=95
#     def Private(self):
#         s=student()
#         print("Public",s.name)
#         print("Private",s._age)
#         print("Protected",s.__marks)


# class Dog:
#     def sound(self):
#         print("Dog barks")
#
# class Cat:
#     def sound(self):
#         print("Cat meows")
# d = Dog()
# c = Cat()
# d.sound()
# c.sound()
#

