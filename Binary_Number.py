n = int(input())
if n < 1:
    print("Please enter a positive integer value for n.")
else:
    for i in range(2**n):
        binary_number = format(i, f'0{n}b')  # Format the binary number with leading zeros
        print(binary_number)
