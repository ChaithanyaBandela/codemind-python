def find_last_even_index(arr):
    last_even_index = None
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            last_even_index = i
    return last_even_index
N = int(input())
arr = list(map(int, input().split()))
last_even_index = find_last_even_index(arr)
print(last_even_index)
