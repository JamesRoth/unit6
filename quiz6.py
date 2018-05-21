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
        if len(line)>=9:
            if line[0] == line[4] and line[4] == line[8]:
                print(line)
                break

def prgm3(num,char):
    for line in file:
        line = line.strip()
        if len(line) == num and line[0] == char:
            print(line)

"""
letter = input("Enter a letter: ")
prgm1(letter)

prgm2()
"""
num = int(input("Enter a length: "))
char = input("Enter a letter: ")
prgm3()
