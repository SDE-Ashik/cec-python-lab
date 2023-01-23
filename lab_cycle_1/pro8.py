# n = input("enter a string:")
# b = n[0]
# k="$"
# print(b)
# c = n[1:]
# print(c)

# d = c.replace(b, k)
# print(d)


# n = input("enter a string:")
# b = n[0]
# k = "$"
# print(b)
# c = n[1:]
# print(c)
# d = b + c.replace(b, k,10)
# print(d)

# n = input("Enter a string:")
# first_char = n[0]
# modified_string = n[1:].replace(first_char, "$", 1)
# output = first_char + modified_string
# print(output)

n = input("enter a string:")
print(n[0] + n[1:].replace(n[0], "$"))
