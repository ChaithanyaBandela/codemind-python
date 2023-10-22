phy,che,bio,math,cs=map(int,input().split())
tot=(phy+che+bio+math+cs)//5
if(tot>=90):
    print("Grade A")
elif tot>=80:
    print("Grade B")
elif tot>=70:
    print("Grade C")
elif tot>=60:
    print("Grade D")
elif tot>=40:
    print("Grade E")
else:
    print("Grade F")