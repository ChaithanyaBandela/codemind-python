def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_product(n):
    for i in range(2, n):
        if n % i == 0 and is_prime(i) and is_prime(n // i):
            return i, n // i
    return -1
n = int(input())
result = find_prime_product(n)
if result == -1:
    print("-1")
else:
    print(result[0], result[1])
