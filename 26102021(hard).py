"""Squeezing is a process in which the digits of a number is squared and summed up. For example, if the number is 345 then after squeezing, we get 32+42+52 = 50.

Repeated squeezing is a process in which squeezing is repeated for a number ‘n’, for some number of iteration. For example, when repeated squeezing is done for two iterations for 345. It looks as follows:

345 -> 32+42+52 = 50

50 -> 52 + 02 = 25

A number n, is said to squeezable to four, if it is possible to get 4 after a squeezing operation in number of iterations less than or equal to 10. For example, 24 can be sequeezed to 4 in two iterations

24 -> 22 + 42 -> 20

20 -> 22 + 02->4

And 500 can be sequeezed to 4 in eight iteration as shown below:

500-> 52 + 02 + 02 -> 25

25 -> 22 + 52 -> 29

29 -> 22 + 92 -> 85

85 -> 82 + 52 ->89

89 -> 82 + 92 -> 145

145 -> 12 + 42 + 52 -> 42

42 -> 42 + 22 -> 20

20 -> 22 + 02 -> 4

Given a number, n, write a code to print the number of iterations required if 'n' is squeezable to four (in number of iterations <=10) and print 'No' otherwise"""
n=input()
l=[]
i=1
flag=True
while i<=10:
    k = list(str(n))
    l=k
    s = 0
    for j in range(len(l)):
        s=s+int(l[j])**2
        n=s

    if s==4:
        flag=False
        break
    i=i+1
if flag==False:
    print(i)
else:
    print("No")