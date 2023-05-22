n=int(input())
x=ord('A')+n-1
for i in range(n,0,-1):
    for j in range(i):
        print(chr(x),end=" ")
    print()
    x=x-1