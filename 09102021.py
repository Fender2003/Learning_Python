"""Four persons are standing in a queue to book takal ticket for a particular train. At a particular point of time,
the number of seats avaiable gets reduced to three. So the ticket issuing person decides to give tickets for three
    seniormost (age wise) persons among the four persons waiting to get the ticket. Each of them in queue had been
    issued a token. Given the token number issued and the age of the four people, write a code to print the token
    number of persons for whom tickets will be issued. Print the token numbers in the order same as the input order.
    For example, if the token numbers and age are as follows:

101, 45

104, 56

109, 38

125, 67
Then print token numbers 101, 104 and 125."""

t1=int(input())
a1=int(input())
t2=int(input())
a2=int(input())
t3=int(input())
a3=int(input())
t4=int(input())
a4=int(input())
l=[a1,a2,a3,a4]
x={a1:t1,a2:t2,a3:t3,a4:t4}
k=min(l)
for i in range(4):
    if k!=l[i]:
        print(x.get(l[i]))