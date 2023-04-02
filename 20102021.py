n1=input()
n2=input()
l1=list(n1)
l2=list(n2)
l1.reverse()
l2.reverse()
flag=False
for i in range(len(l1)):
    if l1[i]==l2[i]:
        if i==0:
            print("Same at %d's position" % ((1)*(10)**i))
        else:
            print("Same at %dth position" % ((1)*(10)**i))
        flag=True
if flag==False:
    print("No digits are same")