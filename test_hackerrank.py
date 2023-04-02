n = input()

# 24 -> 2^2 + 4^2 = 20
# 20 -> 2^2 + 0^2 = 4
c = 0
x = n
num = 0
while num!=4 and c<=10:
    if num!=0:
        x = num
    l = list(str(x))
    num = 0
    for i in range(len(l)):
         num = num + (int(l[i])**2)
    #print(num, end=" ")
    c += 1

if c<=10:
    print(c)
else:
    print("SOrry")

