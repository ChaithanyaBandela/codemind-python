def find_gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a
n, m = map(int, input().split())
gcd = find_gcd(n, m)
print(gcd)
