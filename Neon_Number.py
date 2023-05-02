n=int(input())
su=0
s=n*n
while s>0:
    rem=s%10
    su=su+rem
    s=s//10
if n==su:
    print('Neon Number')
else:
    print('Not Neon Number')