#James Roth
#5/9/18
#fileDemo.py - using and reading files

file = open("engmix.txt")

numWords=0

for line in file:
    numWords+=1

print(numWords)
