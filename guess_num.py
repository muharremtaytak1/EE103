from secret_number import secretNum 

guess_count=0

while True:
    guess=int(input("Enter your guess: "))
    guess_count+=1

    if guess>secretNum:
        print("Too high")
    elif guess<secretNum:
        print("Too low")
    else: 
        print("The same as the secret")
        break
    if guess_count==5:
        break

if guess_count==5 and guess!= secretNum:
    while True:
        print("Oh,noooooo...")