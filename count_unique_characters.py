n=input()
lst=n.lower()
cnt=0
for i in lst:
    if n.count(i)==1 and i!=' ' and i!='':
        cnt+=1
print(cnt)