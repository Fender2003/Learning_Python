#check if 1 and 2 rupee coin can be divided between two person
T = int(input())
l=[]
for i in range(0,T):
    x,y = input().split(" ")
    x=int(x)
    y=int(y)

    if x==0:
        if y%2==0:
            v="YES"
        else:
            v="NO"

    elif x%2==0:
        v="YES"
    else:
        v="NO"
    l.append(v)

for i in l:
    print(i)

