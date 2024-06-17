user_string = input("Enter a string: ")
user_char = input("Enter the starting  character : ")
user_char2 = input("Enter the ending character : ")

if len(user_string) > 0 :
    if user_string[0] == user_char:
        if user_string[-1] == user_char2:
            print(f"The string starts and ends with the given character.")
        else:
            print("the string starts with the given character but doesnot end with the given character .")
    else:
        print(f"The string does not start the character .")
