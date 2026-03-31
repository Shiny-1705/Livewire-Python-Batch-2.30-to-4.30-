'''
#Write a program to handle divide by zero error
try:
    a=int(input("Enter your Number 1:"))
    b=int(input("Enter your Number 2:"))
    result=a/b
    print(result)
except ZeroDivisionError:
    print("Cannot divide by Zero")

#Take input from user and handle wrong input (like text instead of number)
try:
    num=int(input("Enter your Number:"))
    print(num)
except ValueError:
    print("Wrong input")

#Use try and except to stop the program from crashing
try:
    num=int(input("Enter your Number:"))
    result=10/num
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Wrong input")

#Handle more than one error in a single program
try:
    num=int(input("Enter your Number:"))
    result=10/num
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Wrong input")

#Use else block when there is no error
try:
    num=int(input("Enter your Number:"))
    result=10/num
except:
    print("Cannot divide by Zero")
else:
    print("Result:",result)

#Use finally block that runs every time
try:
    num=int(input("Enter your Number:"))
    result=10/num
except:
    print("Cannot divide by Zero")
else:
    print("Result:",result)
finally:
    print("Program finished")

#Create your own exception using raise
age=-5
if age<0:
    raise ValueError("Age cannot be negative")

#Check age and show error if age is less than 18
try:
    age=int(input("Enter your Age:"))
    if age<18:
        raise ValueError("Age should be above 18")
except ValueError:
    print("Invalid input")

#Use multiple except blocks for different errors
try:
    num=int(input("Enter your Number:"))
    result=10/num
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Wrong input")

#Write a program using nested try-except
try:
    num_input=input("Enter the numerator:")
    num=int(num_input)
    try:
        den_input=input("Enter the denominator:")
        den=int(den_input)
        result=num/den
        print(result)
    except ZeroDivisionError:
        print("Cannot divide by Zero")
except ValueError:
    print("Wrong input")
'''
































