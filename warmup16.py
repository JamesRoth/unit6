#James Roth
#5/11/18
#warmup16.py - printing words that start with J and end with R

file = open("engmix.txt")

for item in file:
    if item[0] == "j" and item[-1] == "r":
        print(item)
