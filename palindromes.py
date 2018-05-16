#James Roth
#5/11/18
#plaindromes.py - printing out palindromes

file = open("engmix.txt")

def palindrome(text):
    list1 = []
    text = str(text)
    for i in range(0, len(text)):
        list1.append(text[i])
    list2 = list1[:]
    list2.reverse()
    if list1 == list2:
        palindromes.append(text)

palindromes = []

for item in file:
    item = item.strip("\n")
    if len(item) > 0:
        palindrome(item)

print(palindromes)
