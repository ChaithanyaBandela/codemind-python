def sum_odd_index_elements(arr):
    odd_sum = 0
    for i in range(len(arr)):
        if i % 2 != 0:
            odd_sum = odd_sum+arr[i]
    return odd_sum
N = int(input())
arr = list(map(int, input().split()))
odd_sum = sum_odd_index_elements(arr)
print(odd_sum)
