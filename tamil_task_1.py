#Task 1
#1
'''num1=int(input("Enter your Number 1:"))
num2=int(input("Enter your Number 2:"))
print("Addition is ",num1+num2)
print("Subtraction is ",num1-num2)
print("Multiplication is ",num1*num2)
print("Division is ",num1/num2)
print("Modulus is ",num1%num2)
print("Floor Division is ",num1//num2)
print("Exponentiation is ",num1**num2)'''

#2
'''print("1.Rectangle\n2.Square\n3.Circle")
choice=int(input("Enter your choice:"))
if choice==1:
    length=float(input("Enter the Length:"))
    breadth=float(input("Enter the breadth:"))
    print("The Area of Rectangle is ",length*breadth)
    print("The Perimeter of Rectangle is ",2*(length+breadth))
elif choice==2:
    side=float(input("Enter the side:"))
    print("The Area of Square is ",side*side)
    print("The Perimeter of Square is ",4*side)
elif choice==3:
    radius=float(input("Enter the radius:"))
    print("The Area of Circle is ",3.14*radius*radius)
    print("The Circumference of Circle is ",2*3.14*radius)
else:
    print("Enter a valid choice")'''

#3
'''num1=float(input("Enter your Number 1:"))
num2=float(input("Enter your Number 2:"))
num3=float(input("Enter your Number 3:"))
average=(num1+num2+num3)/3
print("The Average of your 3 numbers are ",average)'''

#4
'''a=int(input("Enter your Number 1:"))
b=int(input("Enter your Number 2:"))
if a==b:
    print("Number 1 is equal to Number 2")
elif a>b:
    print("Number 1 is greater than Number 2")
else:
    print("Number 1 is less than or equal to Number 2")'''

#5
'''number=int(input("Enter your Number:"))
square_root = number**0.5
print("The Square root of a Number is ",square_root)'''

#6
'''print("1.Simple Interest\n2.Compound Interest")
choice=int(input("Enter your Choice:"))
p=int(input("Enter your Principal amount:"))
n=int(input("Enter your Number of years:"))
r=float(input("Enter your Rate of Interest:"))
if choice==1:
    SI=(p*n*r)/100
    print("The Simple Interest is ",SI)
elif choice==2:
    a=p*(1+r/100)**n
    CI=a-p
    print("The Compound Interest is",CI)
else:
    print("Enter a Valid Choice")'''

#7
'''x=10
x+=5
print(x)
x-=3
print(x)
x*=2
print(x)
x/=4
print(x)
x%=2
print(x)
x**=3
print(x)'''

#8
'''a=int(input("Enter your number 1:"))
b=int(input("Enter your number 2:"))
print("Before Swapping : ",a,b)
a=a+b
b=a-b
a=a-b
print("After Swapping : ",a,b)'''

#9
'''username=input("Enter your Username:")
password=input("Enter your password:")
if username=="admin" and password=="1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")'''

#10
'''num=int(input("Enter your Number:"))
cube_root=num**(1/3)
print("The Cube root of your number is ",round(cube_root))'''

#11
'''n=102938
temp=n%100
print("The last Two digit of the Number is ",temp)'''

#12
'''n=102938
result=n//1000
print(result)'''


