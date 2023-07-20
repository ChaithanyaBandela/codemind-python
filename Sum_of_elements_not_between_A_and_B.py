n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
elements_not_between = [num for num in lst if num < a or num > b]
print(sum(elements_not_between))