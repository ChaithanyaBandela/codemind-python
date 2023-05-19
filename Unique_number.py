def is_unique_number(number):
    digit_list = list(str(number))
    return len(digit_list) == len(set(digit_list))

# Example usage
num = int(input())
if is_unique_number(num):
    print("Unique Number")
else:
    print("Not Unique Number")
