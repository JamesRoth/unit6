#James Roth
#5/10/18
#longestDictionaryWord - longest word in dictionary

file = open("engmix.txt")

length = 0
item1 = ""

for item in file:
    if len(item)>length:
        item1 = item
        length = len(item)
