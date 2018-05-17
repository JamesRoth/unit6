#James Roth
#5/17/18
#anagram.py - all the words that are anagrams

file = open("engmix.txt")

list1 = []

def anagram(string, list1):
    if string in list1:
        print(string)

for item in file:
    item = item.strip("\n")
    list2 = []
    for char in item:
        list2.append(char)
    list2.sort()
    word = ""
    for item in list2:
        word+=item
    list1.append(word)

for item in list1:
    anagram(item, list1)
