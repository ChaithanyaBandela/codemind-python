n,k=map(int,input().split())
lst=list(map(int,input().split()))
snt=0
for i in lst:
    if i%k==0:
        snt+=1
print(snt)