#James Roth
#5/11/18
#plaindromes.py - printing out palindromes

file = open("engmix.txt")

for item in file:
    item.strip("\n")
    if len(item) > 0:
