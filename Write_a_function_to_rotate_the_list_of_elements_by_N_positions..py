n=int(input())
lst=list(map(int,input().split()))
a=int(input())
a=(a)%n
lst=(lst[-a:]+lst[:-a])
for i in lst:
    print(i,end=" ")
    