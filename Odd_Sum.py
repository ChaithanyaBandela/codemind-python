def sum_odd_elements(arr):
    odd_sum = 0
    for num in arr:
        if num % 2 != 0:
            odd_sum += num
    return odd_sum

N = int(input())
arr = list(map(int, input().split()))
odd_sum = sum_odd_elements(arr)
print(odd_sum)
