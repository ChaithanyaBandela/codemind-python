n=int(input())
lst=list(map(int,input().split()))
for i in range(0,n):
    if lst[i]==0:
        print(lst[i],end=" ")
for j in range(0,n):
    if lst[j]==1:
        print(lst[j],end=" ")