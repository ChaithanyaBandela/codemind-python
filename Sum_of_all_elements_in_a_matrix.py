r,c=map(int,input().split())
mat=[]
for i in range(r):
    sub_list=list(map(int,input().split()))
    mat.append(sub_list)
s=sum(sum(i) for i in mat)
print(s)
