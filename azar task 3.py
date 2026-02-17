
# numbers from 1 to 10

for i in range(1,11):
    print (i)

#the multiplication table

a = int(input("enter the value:"))
for i in range(1,11):
    print(a,'x',i,'=',a*i)

#all even numbers from 1 to 50
for i in range(1,51):
    if i%2 == 0:
        print (i)

#the factorial of a number

n=int(input("enter the value"))
f=1
for i in range(1,n+1):
    f=f*i
    print("factorial:",f)

#a pattern

for i in range(1,5):
    for j in range(i):
        print('$',end="")
    print()

#even numbers from 2 to 20

for i in range(2,21):
    if i%2 == 0:
        print(i)

#even numbers between 20 to 50.

for i in range(20,51):
    if i%2 == 0:
        print(i)

#the odd numbers using for loop

n = int(input("enter the value of n ="))
m = int (input("enter the value of m ="))
for i in range(n,m):
    if i%2 !=0:
        print (i)

#the hollow paterns

rows = int(input("enter the rows size for the pattern"))
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if i==1 or i==rows or j==1 or j==rows:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#the alphabet numbers from a to z
for i in range(97,123):
    print(chr(i))
