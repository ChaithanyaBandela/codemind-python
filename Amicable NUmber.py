def sum_proper_divisors(n):
    divisors = [1] 
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i: 
                divisors.append(n // i)
    return sum(divisors)

def are_amicable(a, b):
    sum_a = sum_proper_divisors(a)
    sum_b = sum_proper_divisors(b)
    return sum_a == b and sum_b == a

# Example usage
num1 = int(input())
num2 = int(input())
if are_amicable(num1, num2):
    print("Amicable");
else:
    print("Not Amicable")
