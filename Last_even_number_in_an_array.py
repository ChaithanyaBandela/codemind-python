def find_last_even(arr):
    last_even = None
    for num in arr:
        if num % 2 == 0:
            last_even = num
    return last_even
N = int(input())
arr = list(map(int, input().split()))
last_even_number = find_last_even(arr)
print(last_even_number)
