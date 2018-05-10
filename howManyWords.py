#James Roth
#5/10/18
#howManyWords.py - how many words have x length

file = open("engmix.txt")

wordLen = [0]*22

for item in file:
    item.strip()
    wordLen[len(item)-1]+=1

for i in range(0, len(wordLen)):
    print(str(i+1) + "-letter words:", wordLen[i])
