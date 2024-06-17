number = int(input("Enter a number: "))
sum = 0
while number != 0:
    sum = sum + (number % 10)
    number = number //10
print(sum)