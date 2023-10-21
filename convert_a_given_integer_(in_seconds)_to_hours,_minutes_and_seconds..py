n=int(input())
hours=n//3600
minu=(n%3600)//60
sec=(n%3600)%60
print(f"H:M:S-{hours}:{minu}:{sec}")
