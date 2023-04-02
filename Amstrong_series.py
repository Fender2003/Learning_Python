"""An Armstrong number of three digits is an integer such that the
sum of the cubes of its digits is equal to the number itself. For example, 371 is an
Armstrong number since 3**3 + 7**3 + 1**3 = 371."""
for i in range(0,1000):
    l=list(str(i))
    if len(l)==1:
        if int(l[0])**3==i:
            print(i)
    if len(l)==2:
        if int(l[0])**3+int(l[1])**3==i:
            print(i)
    if len(l)==3:
        if int(l[0])**3+int(l[1])**3+int(l[2])**3==i:
            print(i)

