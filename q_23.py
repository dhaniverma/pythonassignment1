print("CHOOSE THE OPTION FROM 1 AND 2 FROM THE GIVEN: ")
print("1. FROM C TO F ")
print("2. FROM F TO C ")
input_num = int(input("Enter your choice: "))
if input_num == 1:
    degree =  int(input("Enter your degree: "))
    calc = 9/5
    F = (calc*degree) + 32
    print("this is F :", F)
if input_num == 2:
    degree2 = int(input("Enter your degree: "))
    calc2 = 5/9
    C = (degree2 - 32) * calc2
    print("this is C  :", C)
else:
    print("Please enter a valid input")