n=int(input())
lst=list(input().split())
cnt=0
for i in lst:
    if len(i)%2==0:
        cnt=cnt+1
print(cnt)