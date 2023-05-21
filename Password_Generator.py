def generate_final_string(input_string):
    pairs = input_string.split(',')
    final_string = ''
    
    for pair in pairs:
        parts = pair.split(':')
        string = parts[0]
        digits = [int(digit) for digit in parts[1] if digit.isdigit()]
        
        if len(digits) == 0:
            final_string += 'X'
        else:
            max_valid_digit = max([digit for digit in digits if digit <= len(string)], default='X')
            if max_valid_digit == 'X':
                final_string += 'X'
            else:
                final_string += string[max_valid_digit - 1].lower()
    
    return final_string
input_str = input()
output_str = generate_final_string(input_str)
print(output_str)
