#James Roth
#5/11/18
#reverseFile.py - user entered file that gets printed backwards

string = input("Enter the name of the file you want to open: ")

file = open(string)

list1=[]

for line in file:
    line=line.strip("\n")
    if len(line)>0:
        list1.append(line)

list1.reverse()
print(list1)
