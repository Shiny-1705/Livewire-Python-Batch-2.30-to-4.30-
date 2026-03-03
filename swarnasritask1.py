1 #arithmetic operator
a=5
b=7
print('add:',a+b)
c=a-b
print('sub:',c)
print(a*b)
print(a/b)
print(a//b)
print(a**b)

2 #rectangle
length=int(input("enter the length of rectangle:"))
breadth=int(input("enter the breadth of rectangle:"))
area_rectangle=length*breadth
perimeter_rectangle=2*(length+breadth)
print("rectangle area=",area_rectangle)
print("rectangle perimeter=",perimeter_rectangle)

#square
side=int(input("enter the side of the square:"))
area=side*side
perimeter=4*side
print("area of the square=",area)
print("perimeter of the square=",perimeter)

#circle
r=int(input("enter the radious of the circle"))
area=3.14*r*r
perimeter=2*3.14*r
print("area of the circl=",area)
print("perimeter of the circle=",perimeter)

3 #question
a=int(input("enter the first value:"))
b=int(input("enter the second value:"))
c-=int(input("enter the thied value:"))
avg=(a+b+c)/3
print("enter the average value=",avg)

4 #question
num1=int(input("enter first number:"))
num2=int(input("enter the second number:"))
if num1==num2:
    print("both numbers are equal.")
else:
    print("numbers are equal.")
    
5 #question
import math
num=int(input("enter anumber:"))
sqrt_num=math.sqrt(num)
print("sqrt of",num,"is",sqrt_num)

6 #question
p=int(input("enter the principle amount:"))
r=int(input("enter the rate of the amount:"))
t=int(input("enter the time in years:"))
si=(p*r*t)/100
ci=p*(1+r/100)**t
print("simple interesr=",si)
print("simple compound=",ci)

7 #assignment operator
x=10
x+=5
x-=3
x*=2
x/=4
x%=2
x**=3
print("final value of x:",x)

8 #question
a=int(input("enter first number:"))
b=int(input("enter second number:"))
print("before swapping")
print("a=",a)
print("b=",b)
a=a+b
b=a-b
a=a-b
print("after swapping:")
print("a=",a)
print("b=",b)

9 #question
username=int(input("enter the username:"))
password=int(input("enter the password:"))
if username=="admin"or password==1812:
    print("login successful!")
else:
    print("invalid username and password.")

10 #question
num=int(input("enter a number:"))
cube_root=num**(1/3)
print("cube root of",num,"is",cube_root)

11 #question
num=102938
last_two_digits=num%100
print("last two digits of",num,"are",last_two_digits)

12 #question
num=102938
result=num//100
print("after removing last 2 digits:",result)
    
                   

                



                

    
        


            
