for i in range(1,11):
    print(i)


a=int(input("Enter The Number:"))
for i in range(1,6):
    print(a,"X",i,"=",a*i)



for i in range(2,51,2):
    print(i)

n=int(input("Enter The Number:"))
f=1
for i in range(1,n+1):
    f=f*i
print("factorial",f)
    
for i in range(1,5):
    print("*" * i)


for i in range(2,21,2):
    print("Even Numbers:",i)
    


for i in range(20,51,2):
    print("Even Numbers:",i)
    



for i in range(1,100,2):
    print("Odd Numbers:",i)





n = 4

for i in range(n):          
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    


    
for i in range(ord('a'), ord('z') + 1):
    print(chr(i), end=" ")

