weight=input("Enter you weight")
unit=input("(l)bs or (k)g: ")
converted=""
if unit.upper() == "L":
    converted=float(weight)*.45
    print(f"you are {converted} kgs ")
else :
    converted=float(weight)/.45
    print(f"you are {converted} pounds ")
