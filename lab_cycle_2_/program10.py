# generate all factors of a number
def factors(n):
    list1 = []
    for i in range(2, n):
        if n % i == 0:
            print(i)
            list1.append(i)
    return list1


print("factors of 35 are ", factors(35))
print("factors of 34 are ", factors(34))
num = int(input("enter a number to find the factors :"))

print(f"factors of {num}are", factors(num))
