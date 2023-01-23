# Store a list of first names .Count the occurences of 'a' within the list

n = int(input("how many numbers do you want to insert:"))
l1 = []
for i in range(n):
    l1.extend(input("enter the name:"))
print(l1.count("a"))
