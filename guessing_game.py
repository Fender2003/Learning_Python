#guessing a number from 0-9 in 3 chances and terminating the program if I get the correct answer
secret_number=9
guess_count=1
guess_limit=3
while guess_count <= guess_limit:
    guess=int(input('Guess: '))
    guess_count+=1
    if guess ==secret_number:
        print("you Win!")
        break
else:
    print("Sorry, you failed")
