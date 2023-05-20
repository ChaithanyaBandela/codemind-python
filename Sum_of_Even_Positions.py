def sum_even_index_elements(arr):
    even_sum = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            even_sum =even_sum+ arr[i]
    return even_sum
N = int(input())
arr = list(map(int, input().split()))
even_sum = sum_even_index_elements(arr)
print(even_sum)
