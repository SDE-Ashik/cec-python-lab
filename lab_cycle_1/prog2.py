# Display future leap year from current year to a final year enter by a user


def leapyear(initial, final):
    print(f"""leap year between {initial}and {final}""")
    for initial in range(initial,final + 1):
        if initial % 4 ==0 :
            if initial%100==0:
                if initial%400==0:
                    print(initial)
            else:
                print(initial)

i = int(input("enter the current year:"))
j = int(input("enter the future year:"))
leapyear(i, j)
