def absolute_difference(arr):
    even_sum = 0
    odd_sum = 0
    for i in arr:
        if i % 2 == 0:
            even_sum =even_sum+i
        else:
            odd_sum=odd_sum+i
    return abs(even_sum - odd_sum)

N = int(input())
arr = list(map(int, input().split()))
diff = absolute_difference(arr)
print(diff)
