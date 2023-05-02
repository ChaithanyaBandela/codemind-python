n=int(input())
su=0
while n>0:
    rem=n%10
    su=(su*10)+rem
    n=n//10
print(su)