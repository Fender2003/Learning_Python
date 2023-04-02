a=input()
b=input()
c=input()
d=input()
def  greet(*args):
    #This function greets all the person in the names tuple.
    for i in args:
        print("Hello",i)
greet(a,b,c,d)
