"""Sum of digit powers of a five digit number is defined as follows:

1^d1 + 2^d2 + 3^d3 + 4^d4 + 5^d5

Where d1 is the right most digit and d5 is the leftmost digit.

For example, Sum of digit powers of 71694 is

1^4 + 2^9 + 3^6 + 4^1 + 5^7

= 79371

Given a five digit number n, write a code to find the sum of digit powers of n."""

n=input()
a=list(n)
print(a)
Sum=0
for x in range(1,len(a)+1):
    Sum=Sum+(x**int(a[5-x]))

print(Sum)
