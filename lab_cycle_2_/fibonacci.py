# fibonacci series of N terms

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


num = int(input("enter the number of terms:\t"))
print(f"fibonacci series are ")
for i in range(0, num ):
    print(fibonacci(i))


# output

# enter the number of terms:	10
# fibonacci series are
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
