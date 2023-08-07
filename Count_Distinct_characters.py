n=input()
ls=n.lower()
l=[]
for i in ls:
    if i!=' ':
        l.append(i)
print(len(set(l)))