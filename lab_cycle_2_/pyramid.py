def pyramid(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(num*j, end=" ")
        num = num + 1
        print()


limit = int(input("enter a number:\t"))
pyramid(limit)
