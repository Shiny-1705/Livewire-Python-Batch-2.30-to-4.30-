                     #task-3
#1.
'''
for i in range(1,10):
    print(i)
'''

#2.
'''
a=int(input("enter  number:"))
for i in range(1,6):
    print(a,"x",i,"=",a*i)'''

#3.
'''
for i in range(1,50):
    if i%2==0:
        print (i)'''

#4.
'''
a=int(input("enter a number:"))
fact=1
for i in range (1,a+1):
    fact=fact*i
    print(fact)'''

#5.
'''
for i in range(1,5):
    for j in range(i):
        print("*",end=" ")
    print()'''

#6.
'''
for i in range(2,20):
    if i%2==0:
        print(i)'''

#7.
'''
for i in range(2,50):
    if i%2==0:
        print(i)'''

#8.
'''
n=int(input("enter a number"))
for i in range(n):
      if i%2!=0:
          print(i)'''

#9.
rows=int(input("enter a number"))
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if i==1 or  i==rows or  j==1 or  j==rows:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#10.
'''
for i in range(97,123):
    print(chr(i))'''
        
     
