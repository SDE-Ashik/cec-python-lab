# find the sum of all items in a list

list1 = []
total = 0
limit = int(input("enter the size of a list :\t"))
for i in range(limit):
    list1.append(int(input(f"{i + 1} element is:\t")))
    # total= total + list[i]
# print(f"elements sum of a list is {total}")
print(f"sum of the elements in a list is ", sum(list1))  #using sum()


# output
# enter the size of a list :	5
# 1 element is:	2
# 2 element is:	3
# 3 element is:	4
# 4 element is:	5
# 5 element is:	6
# sum of the elements in a list is  20