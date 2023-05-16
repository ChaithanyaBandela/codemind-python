n=int(input())
lst=list(map(int,input().split()))
su=0
s=0
for i in range(len(lst)):
    if i%2==0:
        su=su+lst[i]
    elif i%2!=0:
        s=s+lst[i]
if (su-s)==0:
    print("YES")
else:
    print("NO")