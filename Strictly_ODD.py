def is_strictly_odd(arr):
    for i in range(1, len(arr), 2):
        if arr[i] % 2 == 0:
            return False
    return True
n = int(input())
a = list(map(int,input().split()))

strictly_odd= is_strictly_odd(a)
print(strictly_odd)
