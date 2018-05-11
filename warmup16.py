#James Roth
#5/11/18
#warmup16.py - printing words that start with J and end with R

file = open("engmix.txt")

for item in file:
    item=item.strip("\n")
    if len(item) > 0:
        if item[0] == "x" and item[-1] == "d":
            print(item)
