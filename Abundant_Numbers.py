def abundant_number(n):
    su= 0
    for i in range(1, n):
        if n % i == 0:
            su=su+ i

    return su> n
n = int(input())
if abundant_number(n):
    print("True")
else:
    print("False")
