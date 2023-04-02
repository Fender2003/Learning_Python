Name=input("Enter your name")
if len(Name) < 3:
    print("name must be atleast 3 characters")
elif len(Name) > 20:
    print("name must be a maximum 20 characters")
else:
    print("name looks good!")
