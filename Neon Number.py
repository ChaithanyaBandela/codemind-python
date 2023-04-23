n=int(input())
su=0
sq=n*n
while sq>0:
    rem=sq%10
    su=su+rem
    sq=sq//10
if(su==n):
    print("Neon Number")
else:
    print("Not Neon Number")
