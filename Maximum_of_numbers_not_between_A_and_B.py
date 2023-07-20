n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
elements_not_between = [num for num in lst if num < a or num > b]
if not elements_not_between:
        print("-1")
else:
    print(max(elements_not_between))