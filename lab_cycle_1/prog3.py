# List comprehensions
# (a)Generate postive list of numbers from a given list of integers
n = int(input("how many numbers do you want to insert:"))
l1 = []
for i in range(n):
    l1.append(int(input(f"""{i + 1} position number is:""")))

l2 = [x for x in l1 if x >= 0]
print(l2)

# (b) Square of N numbers

num = int(input("enter a limit :"))
print(f"square of 1 to {num}")
l1 = [i ** 2 for i in range(1, num + 1)]
print(l1)

# (c) Form a list of vowels selected from a given word

word = input("enter a word:")
a = "aeiouAEIOU"
l1 = [x for x in word if x in a]
print(l1)


# (d) List ordinal value of each element of a word (Hint use ord() to get ordinal value)

n = input("enter a word:")
l2 = [ord(x) for x in n ]
print(l2)