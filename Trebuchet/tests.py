def find_digit_indexes(input_string):
    digit_words = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    digit_indexes = ''
    for i, char in enumerate(input_string):
        if char.isdigit():
            digit_indexes += char
        elif char == 'z' and input_string[i+1]:
            print("")
            
    return digit_indexes

# Example usage:
input_string = "rtwonenineqxvbgtj4"
result = find_digit_indexes(input_string)
print(result)
