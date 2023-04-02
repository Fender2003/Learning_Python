# make a game to start, stop, help a car then told by the user.
i = ""
started=False
while True:
    i=input("> ").lower()
    if i == "start":
        if started:
            print("car is already started")
        else:
            started=True
            print("Car Started..... Ready to go")


    elif i == "stop":
        if not started:
            print("car is alrady stopped")
        else:
            started=False
            print("Car stopped")


    elif i == "help":
        print('''
start-to start the car
stop- to stop the car
quit-to quit''')


    elif i == "quit":
        break

    else:
        print("I don't understand that")
