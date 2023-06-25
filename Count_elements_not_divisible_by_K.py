n,k=map(int,input().split())
lst=list(map(int,input().split()))
cnt=0
for i in lst:
    if i % k!=0:
        cnt+=1
print(cnt)