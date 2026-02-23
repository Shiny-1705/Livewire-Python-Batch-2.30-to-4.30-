#Task 2
#1
'''number=int(input("Enter the Number:"))
if number%2==0:
    print("The Number is Even")
else:
    print("The Number is Odd")'''

#2
'''number=int(input("Enter your number:"))
if number%2==0 and number%3==0:
    print("Divisible by both")
else:
    print("Not Divisible by both")'''

#3
'''n=int(input("Enter your Number:"))
if n%5==0:
    print("Multiple of 5")
else:
    print("Not Multiple of 5")'''

#4
'''year=int(input("Enter your Year:"))
if (year%4==0 and year%100!=0) or year%400==0:
    print("Leap Year")
else:
    print("Not a Leap year")'''

#5
'''mark1=int(input("Enter your mark 1:"))
mark2=int(input("Enter your mark 2:"))
mark3=int(input("Enter your mark 3:"))
mark4=int(input("Enter your mark 4:"))
mark5=int(input("Enter your mark 5:"))
avg=(mark1+mark2+mark3+mark4+mark5)/5
if avg>=90:
    print("O")
elif avg>=80:
    print("A")
elif avg>=70:
    print("B")
elif avg>=50:
    print("C")
else:
    print("F")'''

#6
'''number=int(input("Enter the Number:"))
if number>0:
    print("Positive")
elif number==0:
    print("Zero")
else:
    print("Negative")'''

#7
'''Has_ticket=input("Do You have ticket(yes/no):")
age=int(input("Enter your Age:"))
if Has_ticket=="yes" and age>=18:
    print("You can enter Party")
else:
    print("You cannot enter Party")'''

#8
'''username=input("Enter your Username:")
if username=="tamil":
    password=input("Enter your Password:")
    if password=="1234":
        print("Login Successful")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")'''

#9
'''character=input("Enter your character:")
if character in ["a","e","i","o","u"]:
    print("Vowel")
else:
    print("Consonant")'''

#10
'''a=int(input("Enter your number 1:"))
b=int(input("Enter your number 2:"))
c=int(input("Enter your number 3:"))
if a>=b and a>=c:
    print("Number 1 is maximum")
elif b>=a and b>=c:
    print("Number 2 is maximum")
else:
    print("Number 3 is maximum")
if a<=b and a<=c:
    print("Number 1 is Minimum")
elif b<=a and b<=c:
    print("Number 2 is Minimum")
else:
    print("Number 3 is Minimum")'''

#11
'''age=int(input("Enter your age:"))
if age>=60:
    print("Senior")
elif age<60 and age>=20:
    print("Adult")
elif age<20 and age>=13:
    print("Teen")
else:
    print("Child")'''

#12
'''num1=float(input("Enter your Number 1:"))
num2=float(input("Enter your Number 2:"))
op=input("Enter your Operator +,-,*,/:")
if op=="+":
    print("Addition is ",num1+num2)
elif op=="-":
    print("Subtraction is ",num1-num2)
elif op=="*":
    print("Multiplication is ",num1*num2)
elif op=="/":
    print("Division is ",num1/num2)
else:
    print("Enter a Valid Operator")'''

#13
'''num=int(input("Enter the number:"))
cube=num**3
print(cube)
if cube>100:
    print("Number's Cube is greater than 100")
elif cube==100:
    print("Number's Cube is equal to 100")
else:
    print("Number's Cube is less than 100")'''

#14
'''year = int(input("Enter the Year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")'''

