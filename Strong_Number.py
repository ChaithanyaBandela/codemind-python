def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_strong_number(num):
    num_str = str(num)
    digit_factorial_sum = sum(factorial(int(i)) for i in num_str)
    
    return digit_factorial_sum == num
num = int(input())
if is_strong_number(num):
    print(f"The number {num} is a strong number")
else:
    print(f"The number {num} is not a strong number")
