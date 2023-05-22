def is_strictly_even(arr):
    for i in range(0, len(arr), 2):
        if arr[i] % 2 != 0:
            return False
    return True
n = int(input())
a = list(map(int,input().split()))
strictly_even = is_strictly_even(a)
print(strictly_even)
