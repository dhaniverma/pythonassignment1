def count_char_frequency(input_string):
    frequency = {}

    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    print(frequency)

count_char_frequency(input("Enter a string: "))
