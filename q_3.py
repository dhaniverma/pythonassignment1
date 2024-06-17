def FACTORIAL(a):
    if a < 0:
        return 0
    elif a == 0 or a ==1:
        return 1
    else:
        factorial = 1
        while (a>1):
                factorial *=a
                a -= 1

        print(factorial)


a = int(input("Enter a number: "))
print(FACTORIAL(a))
