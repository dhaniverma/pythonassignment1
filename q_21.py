input_string = input("Enter the list : ")
input_string = input_string.split()
frequency_dict = {}
for char in input_string:
    frequency_dict[char] = frequency_dict.get(char, 0) + 1
char_to_find = input("Enter the character to find its frequency: ")

if char_to_find in frequency_dict:
    print(f"The frequency of '{char_to_find}' is: {frequency_dict[char_to_find]}")
else:
    print(f"The character '{char_to_find}' is not in the string.")

