'''
#Create a file and write your name
with open("text.txt","w") as f:
    f.write("King Tamil")
    
#Read data from a file
with open("text.txt","r") as f:
    print(f.read())
    
#Add new line to an existing file
with open("text.txt","a") as f:
    f.write("\nreading Python")
    
#Count number of words in a file
with open("text.txt","r") as f:
    data=f.read()
    words=data.split()
    print("Number of Words:",len(words))
    
#Count number of lines in a file
with open("text.txt","r") as f:
    lines=f.readlines()
    print("Number of lines:",len(lines))
    
#Copy data from one file to another
with open("text.txt","r") as f:
    data=f.read()
with open("copy.txt","w") as f1:
    f1.write(data)
    
#Find a word in a file
with open("text.txt","r") as f:
    data=f.read()
    if "King" in data:
        print("word found")
    else:
        print("word not found")
        
#Replace a word in a file
with open("text.txt","r") as f:
    data=f.read()
data=data.replace("reading","writing")
with open("text.txt","w") as f:
    f.write(data)
print("Word replaced")

#Store student name and marks in a file
name=input("Enter your Name:")
marks=input("Enter your Marks:")
with open("data.txt","w") as f:
    f.write(name + " " + marks)
print("Data saved in file")
with open("data.txt","r") as f:
    print(f.read())

#Handle error if file not found
try:
    with open("abc.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
'''
