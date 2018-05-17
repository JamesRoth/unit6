#James Roth
#5/17/18
#warmup17.py - words with all chars of my last name

file = open("engmix.txt")

name = input("Enter your last name: ")

nameChar = []

for char in name:
    if char not in nameChar:
        nameChar.append(char.lower())

for item in file:
    num = 0
    for i in range(0,len(nameChar)):
        if nameChar[i] in item:
            num+=1
    if num == len(nameChar):
        print(item)