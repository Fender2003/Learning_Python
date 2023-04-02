'''Difference of the sum of alternate digits (D)
Given a positive integer 'x' (with even number of digits in it), write an algorithm and the subsequent code to compute the difference between
the sum of the digits occuring in the alternate positions (starting from the first position) and the sum of the digits occuring in the alternate
positions,starting from the last rightmost position of 'x'

For example, consider the number  8975.  The sum of the digits that occur in the alternate positions from the first position is 8+7=15.  The sum
of the digits that occur in the alternate positions, starting from the rightmost position is 5+9 = 14. Difference between the two sums is 1 (=15-14).
Similarly, for the number 5798, the difference between  two sums, is 1.  '''

n=input("Enter a number")
b=[]
d=[]
l=list(n)
print(l)
for a in range(0,len(l),2):
    b.append(l[a])
num1=int(b[0])+int(b[1])
print(num1)

for c in range(1,len(l),2):
    d.append(l[c])
num2=int(d[0])+int(d[1])
print(num2)

print(abs(int(num1)-int(num2)))