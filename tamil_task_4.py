#-----------------Loops----------------------
#Use a for loop to:
#Enter a number between 1 and 100.
'''for i in range(1,101):
    print(i)
'''
#Skip printing if the number is divisible by 3 using continue
'''for i in range(1,21):
    if i%3==0:
        continue
    print(i)
'''
#Stop the loop if the number is divisible by 9 using break
'''for i in range(1,21):
    if i%9==0:
        break
    print(i)
'''
#Use a while loop to:
#Count down from the user’s number to 1
'''n=int(input("Enter the value:"))
while n>=1:
    print(n)
    n-=1
'''
#Use pass when the number is exactly 5
'''for i in range(1,11):
    if i==5:
        pass
    print(i)
'''
#Stop when number is less than 1
'''i=10
while i>=0:
    if i<1:
        break
    print(i)
    i-=1
'''
#Using a for loop, print each letter in the word "PYTHON" except for "H"
'''text="PYTHON"
for i in text:
    if i == "H":
        continue
    print(i)
'''
#Start from 20, count down using while loop
#i.Skip number 17 using continue
#ii.Break at number 13
'''i=20
while i>=1:
    if i==17:
        i-=1
        continue
    elif i==13:
        break
    print(i)
    i-=1
'''

#---------------String--------------------
#Take your name as input and print it in uppercase
'''name=input("Enter your name:")
print(name.upper())
'''
#Take a sentence and convert it into lowercase
'''sentence=input("Enter your sentence:")
print(sentence.lower())
'''
#Enter a sentence and print it with the first letter capitalized
'''sentence=input("Enter any sentence:")
print(sentence.capitalize())
'''
#Use format() to display your name and age in a sentence
'''name=input("Enter your Name:")
age=int(input("Enter your Age:"))
print(f"I am {name} and I am {age} years old")
'''
#Find the index of a given character in a word
'''word=input("Enter any word:")
print(word.index('m'))
'''
#Find the position of a substring in a sentence using find()
'''sentence=input("Enter your sentence:")
substring=input("Enter your substring:")
print(sentence.find(substring))
'''
#Check if a word ends with "ing" using endswith()
'''word=input("Enter your word:")
print(word.endswith('ing'))
'''
#Print a string with tabs (\t) and then use expandtabs() to show spaces
'''text="Hello\tTamil"
print(text.expandtabs())
'''
#Encode a string into UTF-8 using encode()
'''text=input("Enter your text:")
print(text.encode('utf-8'))
'''
#Check if a string contains only digits using isdigit()
'''string=input("Enter your string:")
print(string.isdigit())
'''
#Check if a string is numeric using isnumeric()
'''string=input("Enter your string:")
print(string.isnumeric())
'''
#Check if a string is alphanumeric using isalnum()
'''string=input("Enter your string:")
print(string.isalnum())
'''
#Check if a string contains only ASCII characters using isascii()
'''string=input("Enter your string:")
print(string.isascii())
'''
#Check if a string contains only alphabets using isalpha()
'''string=input("Enter your string:")
print(string.isalpha())
'''
#Insert the word 'hii!!' in your sentence using format
'''word='hii!!'
sentence=input("Enter your sentence:")
print(f"{word} {sentence}")
'''
#---------------------Data structure------------------
#Create a list of 10 numbers and use the following methods:
#append() → Add a new number at the end
#insert() → Insert a number at index 3
#remove() → Remove a specific number
#pop() → Remove the last element
#extend() → Add elements of another list
'''n=[1,2,3,4,5,6,7,8,9,10]
n.append(11)
print("Append :",n)
n.insert(3,12)
print("Insert :",n)
n.remove(12)
print("Remove :",n)
print("Pop :",n.pop())
n.extend([11,12,13])
print("Extend :",n)
'''
#Write a program to count how many times a number occurs in a list (use count())
'''n=[1,2,2,3,4,2,1,4,1]
print("Count :",n.count(4))
'''
#Write a program to find the index of a specific element (use index())
'''n=[1,3,2,5,4,7,6]
print("Index :",n.index(5))
'''
#Create a list and reverse it using the reverse() method
'''List=[1,2,3,4,5]
List.reverse()
print("Reverse :",List)
'''
#Sort a list of numbers in ascending and descending order (use sort())
'''List=[1,3,5,7,9,8,6,4,2]
List.sort()
print("Sorted List in Ascending order:",List)
List.reverse()
print("Sorted List in Descending order :",List)
'''
#Remove all elements from a list (use clear())
'''List=[1,2,3,4,5,6,7]
List.clear()
print("Clear :",List)
'''
#Copy a list into another variable (use copy())
'''List=[1,2,3,4,5]
Copy=List.copy()
print("List :",List)
print("Copy :",Copy)
'''
#---------------------Tuple Tasks with Method----------------------
#Create a tuple of numbers and:
#Find the length (use len())
#Find the maximum and minimum values (use max(), min())
'''Tuple=(1,3,5,7,9,8,6,4,2)
print("Length :",len(Tuple))
print("Maximum Value :",max(Tuple))
print("Minimum Value :",min(Tuple))
'''
#Write a program to count how many times an element occurs in a tuple (use count())
'''Tuple=(1,2,1,3,4,5,3)
print("Count :",Tuple.count(1))
'''
#Write a program to find the index of an element in a tuple (use index())
'''Tuple=(1,3,5,7,9,11)
print("Index :",Tuple.index(9))
'''
#Convert a tuple into a list, add some elements, then convert it back into a tuple
#Concatenate two tuples and print the result
#Slice a tuple to print elements from index 2 to 5
'''Tuple=(1,2,3,4,5,6,7,8)
print(Tuple[2:5])
'''
#Check if a given element exists in a tuple (using in operator)
'''Tuple=(1,2,3,4,5,6,7)
print(4 in Tuple)
'''
#-----------Set-----------
'''
#Create a set of 5 numbers and print it
Set={1,2,3,4,5}
print("Set is ",Set)
#Add a new element to the set using add()
Set.add(6)
print("Add :",Set)
#Add multiple elements to a set using update()
Set.update({7,8,9})
print("Update :",Set)
#Remove an element from a set using remove()
Set.remove(9)
print("Remove :",Set)
#Remove an element using discard() and observe the difference from remove()
Set.discard(10)
print("Discard :",Set)
Set.remove(5)
print("Remove :",Set)
#Remove a random element from a set using pop()
Set.pop()
print("Pop :",Set)
#Clear all elements from a set using clear()
Set.clear()
print("Clear :",Set)
'''
#Create two sets and find their:
#Union
#Intersection
'''a={1,2,3,4,5}
b={4,5,6,7,8}
print("Union :",a.union(b))
print("Intersection :",a.intersection(b))
#Find the difference between two sets
print("Diff :",a.difference(b))
#Find the symmetric difference between two sets
print("Symmetric difference :",a.symmetric_difference(b))
'''
#Check whether one set is a subset of another
'''a={1,2,3,4,5}
b={4,5}
print(a.issubset(b))
print(b.issubset(a))
'''
#Convert a list with duplicate values into a set
#Check whether a given element exists in a set using in
'''Set={1,2,3,4,5}
print(5 in Set)
'''
#-----------------DICTIONARY--------------
#Create a dictionary with student name and marks
'''Dict={"Name":"Tamil","Mark":97}
print("Dictionary :",Dict)
#Print all keys of the dictionary
print("Keys :",Dict.keys())
#Print all values of the dictionary
print("Values :",Dict.values())
#Print all key-value pairs using items()
print("Items :",Dict.items())
#Access the value of a specific key
print("Specific key value is", Dict.get("Name"))
#Add a new key-value pair using update()
Dict.update({"Age":21})
print("Update :",Dict)
#Remove a key using pop()
print("Pop :",Dict.pop("Mark"))
print(Dict)
#Remove the last inserted item using popitem()
print("Popitem :",Dict.popitem())
#Check whether a key exists in a dictionary using inCheck whether a key exists in a dictionary using in
print("Age" in Dict)
print("Name" in Dict)
#Clear all elements from a dictionary
print(Dict.clear())
'''






































