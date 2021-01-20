try:
    n = int(input("Enter num: "))
    print(n)
    v = 10 / 0
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Not a number")