#so just because of user mistake the whole program should not crash
#Thus we use Exception handling to get a proper error

try:
    age=int(input('Age: '))
    income=2000
    risk=income/age
    print(age)#if we enter a string instead of integer than it will give an error
except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("Age cannot be zero")