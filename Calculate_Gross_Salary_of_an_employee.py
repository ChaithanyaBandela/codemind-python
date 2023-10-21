salary=float(input())
hra=float(input())
da=float(input())
pf=0.12*salary
gs=salary+hra+da+pf
print(f"{pf:.2f}")
print(f"{gs:.2f}")