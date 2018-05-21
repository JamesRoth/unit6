#James Roth
#5/21/18
#quiz6.py

file = open("engmix.txt")

def prgm1(char):
    for line in file:
        if line.count(char) == 4:
            print(line)

def prgm2():
    for line in file:
        if line[0] == line[4] and line[4] == line[8]:
            print(line)
            break

"""
letter = input("Enter a letter: ")
prgm1(letter)
"""
prgm2()
