# generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square
list1 = []
j = 32
i = int(input("initial range :"))
n = int(input("final range "))
for i in range(n + 1):
    if j ** 2 == i:
        if i % 2 == 0:
            list1.append(i)
        j = j + 1
print(list1)
while (i < n + 1):
    if j ** 2 == i:
        if i % 2 == 0:
            list1.append(i)
        j = j + 1
    i = i + 1
print(list1)

# output
# initial range :1000
# final range 1300
# [1024, 1156, 1296]
# [1024, 1156, 1296]

# using function
def four_digit(n):
    list2 = []
    k = 32
    m = 1000
    if n < 1000:
        print("given range must be greater than 999")
    else:
        while m < n + 1:
            if k ** 2 == m:
                if m % 2 == 0:
                    list2.append(m)
                k = k + 1
            m = m + 1
        return list2

limit = int(input("enter a 4 digit number :\t "))
print(f"four digit perfect even squares are ",four_digit(limit))


# output
# enter a 4 digit number :	 1300
# four digit perfect even squa res are  [1024, 1156, 1296]