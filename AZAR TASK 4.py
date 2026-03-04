                        #LOOPS
'''

#1

for i in range(1,101):
    print(i)

#2

num = int(input("Enter a number between 1 and 100: "))

for i in range(1, num + 1):
    if i % 9 == 0:
        break
    print(i)
#3

a = int(input("Enter a number between 1 and 100: "))

for i in range(1, num + 1):
    if i % 3 == 0:
        continue
    print(i)

#4

a = int(input("Enter a number: "))

while a >= 1:
    if a == 5:
        pass
    else:
        print(a)
    a -= 1

#5

for letter in "PYTHON":
    if letter == "H":
        continue
    print(letter)
    
#6

num = 20

while num >= 1:
    if num == 17:
        num -= 1
        continue
    if num == 13:
        break
    print(num)
    num -= 1


                                  #STRING
    
#1

print("upper")
a = input("Enter your name: ")
print(a.upper())

#2
print("lower")
a = input("Enter a sentence: ")
print(a.lower())

#3
print("capitalize")
a = input("Enter a sentence: ")
print(a.capitalize())

#4
print("format")
name = input("Enter name: ")
age = input("Enter age: ")

print("My name is {} and I am {} years old".format(name, age))


#5
print("index")
word = input("Enter a word: ")
ch = input("Enter a character: ")

print(word.index(ch))

#6
print("find")
sentence = input("Enter sentence: ")
sub = input("Enter substring: ")

print(sentence.find(sub))

#7
print("endswith")
word = input("Enter a word: ")

if word.endswith("ing"):
    print("Ends with ing")
else:
    print("Does not end with ing")
    
#8
print("expandtabs")
a = "Hello\tWorld"
print(a)
print(a.expandtabs())

#9
print("encode")
a = "Python"
print(a.encode("utf-8"))

#10
print("isdigit")
a = input("Enter value: ")
print(a.isdigit())

#11
print("isnumeric")
a = input("Enter value: ")
print(a.isnumeric())


#12
print("isalnum")
a = input("Enter value: ")
print(a.isalnum())

#13
print("isascii")
a = input("Enter value: ")
print(a.isascii())


#14
print("isalpha")
a = input("Enter value: ")
print(a.isalpha())

#15
print("format")
a = "This is {}"
print(a.format("hii!!"))


                            #LIST

#1

nums = [1,2,3,4,5,6,7,8,9,10]

nums.append(11)
nums.insert(3, 100)
nums.remove(5)
nums.pop()
nums.extend([20,30])

print(nums)

#2
print("count")
nums = [1,2,3,2,4,2]
print(nums.count(2))

#3
print("index")
a = [1,2,3,2,4,2]
print(nums.index(3))

#4
print("reverse")
a = [1,2,3,2,4,2]
nums.reverse()
print(nums)

#5
print("sort")
a = [1,2,3,2,4,2]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

#6
print("clear")
a = [1,2,3,2,4,2]
nums.clear()
print(nums)


#7
print("new_list")
a = [1,2,3,2,4,2]
new_list = a.copy()
print(new_list)

'''



                                #TUPLE

#1

t = (10,20,30,40,50)

print(len(t))
print(max(t))
print(min(t))
print(t.count(20))
print(t.index(30))

#2

t = (1,2,3)
l = list(t)
l.append(4)
t = tuple(l)
print(t)

#3

t1 = (1,2)
t2 = (3,4)
print(t1 + t2)


#4

t = (1,2,3,4,5,6)
print(t[2:5])

#5

t = (1,2,3,4,5,6)
print(3 in t)


                                    #SET

#1

s = {1,2,3,4,5}
s.add(6)
s.update([7,8])
s.remove(2)
s.discard(10)
s.pop()
print(s)

#2

a = {1,2,3}
b = {3,4,5}

print(a | b)  # Union
print(a & b)  # Intersection
print(a - b)  # Difference
print(a ^ b)  # Symmetric difference
print(a.issubset(b))

                                #dictionary

#1


student = {"name":"Azar", "marks":85}

print(student.keys())
print(student.values())
print(student.items())

print(student["name"])

student.update({"age":21})
student.pop("age")
student["city"] = "OMALUR"
student.popitem()

print("name" in student)

student.clear()


#2

num = [1,2,2,3,3,3]
f = {}

for i in num:
    f[i] = f.get(i, 0) + 1

print(f)

#3


d1 = {"a":1}
d2 = {"b":2}

d1.update(d2)
print(d1)


#4

d = {"a":10, "b":50, "c":30}
print(max(d, key=d.get))




















































































#
