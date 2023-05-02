n=int(input())
su=0
pro=1
while n>0:
    rem=n%10
    su=su+rem
    pro=pro*rem
    n=n//10
if su==pro:
    print('Spy Number')
else:
    print('Not Spy Number')