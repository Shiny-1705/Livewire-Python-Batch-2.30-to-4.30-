#1 length of a string
'''
a=str(input('enter the string : '))
length= len(a)
print("enter the length of string",length)

#2 maximum value of the number

a=int(input("enter the 1st value"))
b=int(input("enter the 2nd value"))
c=int(input("enter the 3rd value"))
d=int(input("enter the 4th value"))
numbers=[a,b,c,d]
print('the maximum value',max(numbers))


#3 minimum value of the number

a=int(input("enter the 1st value"))
b=int(input("enter the 2nd value"))
c=int(input("enter the 3rd value"))
d=int(input("enter the 4th value"))
numbers=[a,b,c,d]
print('the minimum value',min(numbers))


#4 sum of the number

a=int(input("enter the 1st value"))
b=int(input("enter the 2nd value"))
c=int(input("enter the 3rd value"))
d=int(input("enter the 4th value"))
numbers=[a,b,c,d]
total=sum(numbers)
print('sum',(total))

#5 number is a palindrome or not

a=int(input('enter the value'))
b=0
t=a
while t>0:
    d=t%10
    b=(b*10)+d
    t=t//10
print(b)
if a==b:
    print('p')
else:
    print('N P')

#6  positional arguments.

def student(name,roll_no,dept):
    print("Name    :",name)
    print("Roll no :",roll_no)
    print("Dept    :",dept)
student('azar','66',"IT")

#7  calculate the total marks of a student using positional.
mark1=int(input("enter the M1"))
mark2=int(input("enter the M2"))
mark3=int(input("enter the M3"))
def cal_total(mark1,mark2,mark3):
    total = (mark1+mark2+mark3)
    print("total mark = ",total)
cal_total(mark1,mark2,mark3)


#8 the area of a rectangle

a=int(input('enter the length = '))
b=int(input('enter the width = '))
def ret_area(length,width):
    area= length*width
    print('ret area',area)
ret_area(a,b)

#9  a greeting using default argument.

def greet_user(name,msg ="good morning"):
    print(name,msg)
greet_user("azar")

#10 sum of any number of values


def add_numbers(*args):
    return sum(args)
print(add_numbers(10,20,30))
print(add_numbers(5,7,15,25))


#11 multiplies any number of values

def multiple_all(*args):
    result = 1
    for i in args:
        result = result*i
    print("multiplication : ",result)
multiple_all(2,3,4)



'''










