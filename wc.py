#James Roth
#5/17/18
#wc.py - takes a file and prints out # of lines, # of words, # of chars

fileName = input("Enter the name of the file you want: ")

file = open(fileName)

lines = 0
words = 0
chars = 0

for item in file:
    item = item.strip("\n")
    lines+=1
    num = []
    num = item.split(" ")
    words+=len(num)
    chars+=len(item)
    
print(lines)
print(words)
print(chars)
