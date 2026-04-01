with open("file1.txt","w")as f:
    f.write("Dharani")


with open("file1.txt","r")as f:
    data=f.read()
    print(data)


with open("file1.txt","a")as f:
    f.write("\nThis is a new line")


with open("file1.txt","r")as f:
    data=f.read()
    words=data.split()
    print("Number of words:",len(words))


with open("file1.txt","r")as f:
    lines=f.readlines()
    print("Number of lines:",len(lines))



with open("file1.txt","r")as f1:
    data=f1.read()
with open("file2.txt","w")as f2:
    f2.write(data)


word=input("Enter word to search:")
with open("file1.txt","r")as f:
    data=f.read()
    if word in data:
        print("word found")
    else:
        print("word not found")


old_word=input("Enter word to replace:")
new_word=input("Enter new word:")
with open("file1.txt","r")as f:
    data=f.read()
data=data.replace(old_word,new_word)
with open("file1.txt","w")as f:
    f.write(data)



with open("students.txt","a")as f:
    name=input("Enter student name:")
    marks=input("Enter marks:")
    f.write(name+"-"+marks+"\n")


try:
    with open("nofile.txt","r")as f:
        print(f.read())
except FileNotFoundError:
    print("file not found")
