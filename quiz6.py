#James Roth
#5/21/18
#quiz6.py

file = open("engmix.txt")

def prgm1(char):
    for line in file:
        if line.count(char) == 4:
            print(line)

letter = input("Enter a letter: ")
prgm1(letter)
