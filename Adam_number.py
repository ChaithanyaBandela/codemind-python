n=int(input())
s=n*n
su=0
while n>0:
    rem=n%10
    su=(su*10)+rem
    n=n//10
sq=su*su
sm=0
while sq>0:
    r=sq%10
    sm=(sm*10)+r
    sq=sq//10
if sm==s:
    print('True')
else:
    print('False')