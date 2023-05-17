def is_pronic(n):
    for i in range(int(n ** 0.5) + 1):
        if i * (i + 1) == n:
            return True
    return False

num = int(input())
if is_pronic(num):
    print("YES")
else:
    print("NO")
