#James Roth
#5/17/18
#warmup17.py - words with all chars of my last name

file = open("engmix.txt")

name = input("Enter your last name: ")

nameChar = []

for char in name:
    if char ! in nameChar:
        nameChar.append(char)
