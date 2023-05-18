def is_ugly(num):
    if num <= 0:
        return False
    
    while num % 2 == 0:
        num= num//2
    while num % 3 == 0:
        num =num// 3
    while num % 5 == 0:
        num=num//5
    
    return num==1
def print_num(num):
    if is_ugly(num):
        print('Ugly Number')
    else:
        print('Not Ugly Number')
num=int(input())
print_num(num)
