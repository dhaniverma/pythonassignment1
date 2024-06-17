n = int(input("Enter number of times for series : "))
first_number = 0
second_number = 1
next_number = second_number
count = 1
while count <= n:
    print(next_number, end= ' ')
    count = count + 1
    first_number , second_number = second_number,  next_number
    next_number = first_number + second_number
print()
