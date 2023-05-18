def perfect_square(num):
    if num< 0:
        return False
    if num == 0 or num == 1:
        return True

    left = 1
    right = num // 2
    while left <= right:
        n= (left + right) // 2
        square = n* n
        if square == num:
            return True
        elif square < num:
            left = n + 1
        else:
            right = n - 1

    return False
num=int(input())
print(perfect_square(num))
