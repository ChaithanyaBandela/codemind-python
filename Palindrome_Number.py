def is_palindrome(num):
    num_str = str(num)
    if num_str == num_str[::-1]:
        return True
    else:
        return False
T = int(input())
for _ in range(T):
    num = int(input())
    if is_palindrome(num):
        print("True")
    else:
        print('False')
