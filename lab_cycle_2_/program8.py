n = int(input("enter the size of a list :"))
d = {}
list1 = []
for i in range(n):
    list1.append(input(f" enter the {i + 1} word:  "))
    d[list1[i]] = len(list1[i])
    lo = max(d, key=d.get)
# print(lo)
print(d)
print(list1)
print(lo)