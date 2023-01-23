# write lambda functions to find area of square,rectangle,triangle

# area of a square
side = int(input("enter  side of a square:"))

area = lambda a: a**2
print(f"area of square = ",area(side))
# area of rectangle
len =int(input("enter length of a rectangle:"))
bre =int(input("enter breadth of a rectangle:"))
area = lambda a,b:a*b
print(f"area of rectangle=",area(len,bre))

# area of a triangle
base = int(input("enter the base:"))
height = int(input("enter the height:"))
area = lambda a,b:(a*b)/2
print(f"area of triangle=",area(base,height))

# output
# enter  side of a square:5
# area of square =  25
# enter length of a rectangle:3
# enter breadth of a rectangle:2
# area of rectangle= 6
# enter the base:5
# enter the height:3
# area of triangle= 7.5
