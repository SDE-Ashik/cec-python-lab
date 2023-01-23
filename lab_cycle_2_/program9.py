# Counstruct following pattern using nest loop
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

def star(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()
    for i in range(n - 1, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

num = int(input("enter the size :"))
star(num)

# output
# enter the size :5
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
