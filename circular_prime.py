def prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
n=input()
s=int(n)
r=int(n[::-1])
if prime(s):
    if prime(r):
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')