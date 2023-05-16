n=int(input())
lst=list(map(int,input().split()))
cnt=0
cnt1=0
for i in lst:
    if i%2==0:
        cnt=cnt+1
    elif i%2!=0:
        cnt1=cnt1+1
print(cnt,cnt1)