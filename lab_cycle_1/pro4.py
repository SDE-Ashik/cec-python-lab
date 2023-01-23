sentence = input("enter a sentance:")
word = sentence.split()
l1 = dict()
for x in word:
    l1[x] = word.count(x)
print(l1)
