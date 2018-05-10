#James Roth
#5/10/18
#LastWordDemo.py - prints the last word of each line of a file

file = open("fileDemo.py")

for line in file:
    print(line.strip())
