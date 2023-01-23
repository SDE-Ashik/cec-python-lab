#factorial of a number

def fact(n):
    if n <= 0:
        return 1
    else:
        return n * fact(n - 1)


num = int(input("enter a number :"))
print(f"factorial of {num}! is {fact(num)}")


# output
# enter a number :5
# factorial of 5! is 120
