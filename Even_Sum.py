def sum_even_elements(lst):
    even_sum = 0
    for num in lst:
        if num % 2 == 0:
            even_sum =even_sum+num
    return even_sum

# Input
N = int(input())
arr = list(map(int, input().split()))
even_sum = sum_even_elements(arr)
print(even_sum)
