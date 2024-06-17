def calculator(a,b):
    choice = input("Enter the program to function : ")
    if choice == "+":
        print(a+b)
    elif choice == "-":
        print(a-b)
    elif choice == "*":
        print(a*b)
    elif choice =="/":
        print(a/b)
    else:
        print("Invalid input")
        print("please try again")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
calculator(a,b)