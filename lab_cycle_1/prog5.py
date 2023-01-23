# Prompt the user for a list of integers.for all values greater than 100,store "over" instead

n = int(input('enter a limit:'))
l1 = []
for i in range(n):
    m = int(input(f"{i + 0}.value:-"))
    if m < 101:
        l1.append(m)
    else:
        l1.append("over")
print(l1)
