#James Roth
#5/17/18
#wc.py - takes a file and prints out # of lines, # of words, # of chars

fileName = input("Enter the name of the file you want: ")

file = open(fileName)

lines = 0
words = 0
chars = 0

for item in file:
    line.strip("\n")
    lines+=1
    words+=line.strip(" ")
    chars+=len(line)
    
print(lines)
