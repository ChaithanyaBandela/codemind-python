r,c=map(int,input().split())
mat=[]
for i in range(r):
    sublist=list(map(int,input().split()))
    mat.append(sublist)
s=sum([sum(mat[i]) for i in range(r) if i%2==0])
o=sum([sum(mat[i]) for i in range(r) if i%2!=0])
print(f'{s} {o}')