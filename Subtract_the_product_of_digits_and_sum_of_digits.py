def spy_number(n):
    su=0
    pro=1
    while n>0:
        rem=n%10
        su=su+rem
        pro=pro*rem
        n=n//10
    return pro-su
n=int(input())
print(spy_number(n))
