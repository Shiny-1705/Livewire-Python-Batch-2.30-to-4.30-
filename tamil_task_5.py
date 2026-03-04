#Find the length of a string
'''string=input("Enter your string :")
print("Length :",len(string))
'''
#Find the maximum value of the number
'''n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
n3=int(input("Enter number 3:"))
print(max(n1,n2,n3))
'''
#or
'''numbers=[13,4,56,44,17]
print("Maximum Value is", max(numbers))
'''
#Find the minimum value of the number
'''n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
n3=int(input("Enter number 3:"))
print(min(n1,n2,n3))
'''
#or
'''numbers=[13,4,56,44,17]
print("Minimum Value is", min(numbers))
'''
#Find the sum of the number
'''n=int(input("Enter the number:"))
total=0
for i in range(1,n+1):
    total+=i
print("Sum of the numbers :",total)
'''
#Check whether a number is a palindrome or not
'''num=int(input("Enter your Number:"))
reverse=0
temp=num
while temp>0:
    digit=temp%10
    reverse=(reverse*10)+digit
    temp//=10
if num==reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")
'''
#or using string
'''n=input("Enter your String :")
reverse=n[::-1]
if n==reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")
'''
#Write a function student_details(name, roll, dept) that prints the details using positional arguments
'''def student_details(name,roll,dept):
    print("Name :",name)
    print("Roll No :",roll)
    print("Department :",dept)
student_details("Tamil",17,"CSE")
'''
#Write a function calculate_total(marks1, marks2, marks3) to calculate the total marks of a student using positional
'''def calculate_total(marks1,marks2,marks3):
    total=marks1+marks2+marks3
    print("Total :",total)
calculate_total(50,50,50)
'''
#Write a function rectangle_area(length, width) that calculates the area of a rectangle using positional argument
'''def rectangle_area(length, width):
    area=length*width
    print("Area of Rectangle :",area)
rectangle_area(5,5)
'''
#Write a function greet_user(name, message="Good Morning") that prints a greeting using default argument
'''def greet_user(name, message="Good Morning"):
    print(name,message)
greet_user("Tamil")'''
#Write a function add_numbers(*args) that returns the sum of any number of values
'''def add_numbers(*args):
    total=0
    for i in args:
        total+=i
    print("Total :",total)
add_numbers(5,5,5)
'''
#Write a function multiply_all(*args) that multiplies any number of values
'''def multiply_all(*args):
    product=1
    for i in args:
        product*=i
    print("Multiply all :",product)
multiply_all(10,10,10)
'''
    
    









































































