'''
a=int(input("ENTER A NUMBER :"))
if a%2==0:
      print("EVEN")
else:
    print("odd")



x=int(input("ENTER A NUMBER :"))
if x%2==0 and x%3==0:
    print("Divisible by both")
else:
    print("Not divisible by both")




b=int(input("ENTER A NUMBER :"))
if b%5==0:
    print("Multiple of 5")
else:
    print("Not a multiple of 5")



c=int(input("ENTER A YEAR :"))
if c%4==0:
    print("Leap year")
else:
    print("Not leap year")


a=int(input("ENTER THE NUMBER:"))
if (a<100)and(a>=90) :
      print("A GRADE")
elif (a<=90)and (a>80):
    print("B GRADE")
elif (a<=80) and (a>70):
    print("C GRADE")
elif (a<=70) and (a>60):
    print("D GRADE")
elif (a<=60) and (a>50):
    print("E GRADE")
else:
    print("FAIL")
      



y=int(input("ENTER THE NUMBER:"))
if y>0:
    print("POSITIVE")
elif y<0:
    print("NEGATIVE")
else:
    print("ZERO")


b=int(input("ENTER A AGE:"))
if(b>18):
    print("eligible for party")
else:
    print("You are not eligible")





Username=(input("ENTER THE USERNAME:"))
Password=(input("ENTER THE PASSWORD:"))
if Username=="akash" and Password=="000":
    print("USERNAME AND PASSWORD IS CORRECT:")
else:
    print("INVALID USERNAME AND PASSWORD")


vowels=(input("ENTER THE VOWELS:"))
if vowels=="a,e,i,o,u":
    print("VOWELS SOUND")
else:
    print("CONSONANT")



a=int(input("ENTER THE NUMBER:"))
b=int(input("ENTER THE NUMBER:"))
c=int(input("ENTER THE NUMBER:"))
d=int(input("ENTER THE NUMBER:"))
print(max(a,b,c,d))
print(min(a,b,c,d))


age=int(input("ENTER THE AGE:"))
if age<=12:
    print("CHILD")
elif 13<= age <=19:
    print("TEEN")
elif 20<= age <=50:
    print("ADULT")
elif 51<= age <=60:
    print("SENIOR")
else:
    print("INVALID")






x=int(input("ENTER THE NUMBER:"))
y=int(input("ENTER THE NUMBER:"))
print("Choose operation: +, -, *, /")
z = input("ENTER OPERATION: ")
if z == '+':
    print("ADD:", x + y)
elif z == '-':
    print("SUBTRACTION:", x - y)
elif z == '*':
    print("MULTIPLICATION:", x * y)
elif z == '/':
    print("DIVIDE:",x / y)
else:
    print("INVALID OPERATION")





A = int(input("Enter a number: "))
cube = A ** 3
if cube > 100:
    print("Is greater than 100.")
else:
    print("Is less than or equal to 100.")



'''


year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Is a Leap Year.")
        else:
            print("Is not a Leap Year.")
    else:
        print("Is a Leap Year.")
else:
    print(" Is not a Leap Year.")




























































