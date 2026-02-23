#Task 3

#1
'''for i in range(1,11):
    print(i)
'''

#2
'''n=int(input("Enter the Value:"))
for i in range(1,11):
    print(i,"x",n,"=",n*i)
'''

#3
'''for i in range(2,51,2):
    print(i)
'''
#or
'''for i in range(1,51):
    if i%2==0:
        print(i)
'''

#4
'''n=int(input("Enter your Number:"))
fact=1
for i in range(1,n+1):
    fact*=i
print("Factorial is ",fact)
'''

#5
'''for i in range(1,5):
    for j in range(i):
        print("*" ,end="")
    print()
'''

#6
'''for i in range(2,21,2):
    print(i)
'''
#or
'''for i in range(1,21):
    if i%2==0:
        print(i)
'''

#7
'''for i in range(20,51,2):
    print(i)
'''
#or
'''for i in range(20,51):
    if i%2==0:
        print(i)
'''

#8
'''for i in range(1,21,2):
    print(i)
'''
#or
'''for i in range(1,21):
    if i%2!=0:
        print(i)
'''

#9
'''n=int(input("Enter the value:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or i==n or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''

#10
'''
for i in range(65,91):
     print(chr(i+32))
'''

