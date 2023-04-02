n=int(input("Enter a number"))

for j in range(2,n+1):
    l=[]
    for i in range(1,j+1):
        if j%i==0:
            l.append(i)
    if len(l)==2:
        print(j)



