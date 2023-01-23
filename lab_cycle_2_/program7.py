# add "ing" at the end  of a given string .if it is already end with "ing" ,then add "ly"

s = input("enter a string :\t")
p = s[:-3]
c = "ing"
b = "ly"

# print(s[:-3])
# print(s[-3:])
# a = "ing"
if len(s) < 3 or s[-3:] != c:
    print(s + c)


else:

    print(p + b)


# output
# enter a string :	jump
# jumping