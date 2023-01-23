# enter 2 lists of integers check (A) Whether list of same length (b) whether lists sum to same value (c)whether any value occur in both
c1 = 0
c2 = 0
l1 = []
l2 = []
l3 = []
n = int(input("enter the size of first lisit:"))
print("enter the elements of first list:\n")
for i in range(n):
    k = int(input())
    c1 = c1 + k
    l1.append(k)
print(l1)
m = int(input("enter the size of second lisit:"))
print("enter the elements of second list:\n")
for i in range(m):
    z = int(input())
    c2 = c2 + z
    l2.append(z)
print(l2)
print('''comparing size of both list''')
if len(l1) == len(l2):
    print(f"""both list have same size """)
elif len(l1) > len(l2):
    print(f"first list is greater than second list")
else:
    print(f"second list is greater than first list")


print("comparing sum of both list are same")
if c1==c2:
    print(f"sum of both list are {c1}")
else:
    print(f"not same")
for i in l1:
    for j in l2:
        if i==j:
            l3.append(i)
print("any value occur in both list")
print(l3)