#James Roth
#5/11/18
#reverseFile.py - user entered file that gets printed backwards

string = input("Enter the name of the file you want to open: ")

file = open(string)

list1=[]

for line in file:
    line=line.strip("\n")
    if len(line)>0:
        for i in range(len(line), 1, -1):
            list1.append(line[i-1])

for item in list1:
    print(item)
