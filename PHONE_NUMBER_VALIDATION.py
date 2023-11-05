n=int(input())
s=str(n)
if s[0]=='0':
        print("Invalid")
elif len(s)<10:
    print("Invalid")
else:
    print("Valid")