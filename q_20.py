listno = int(input("Enter the max amount of number for the list to enter : "))
total = 0
index = 0
while index < listno:
    num = int(input("Enter the number  : "))
    total += num
    index +=1

print("the sum of the numbers added in the list is :",total)