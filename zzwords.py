#James Roth
#5/10/18 
#zzwords.py - all the words with zz in the file

file = open("engmix.txt")

for item in file:
    if "zz" in item:
        print(item)