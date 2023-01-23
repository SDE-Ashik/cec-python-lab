# Count  the number of characters (character frequency ) in a string

s = input("enter a string:")
t = []
d = {}
for x in s:
    t.append(x)

for x in t:
    # s.count(x)
    d[x] = s.count(x)
print(d)


# output
# enter a string:muhammadashik
# {'m': 3, 'u': 1, 'h': 2, 'a': 3, 'd': 1, 's': 1, 'i': 1, 'k': 1}