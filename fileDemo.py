#James Roth
#5/9/18
#fileDemo.py - using and reading files

file = open("engmix.txt")

numWords=0

for line in file:
    if "smed" in line:
        print(word)
    numWords+=1

print(numWords)
