while True:

    num=int(input("Enter an integer: "))
    guess=0
    abs_num=abs(num)

    while guess**3< abs_num:
        guess+=1
    if guess**3== abs_num:
        if num<0:
            guess= -guess

        print(f"Cube root of {num} is {guess}")
    else:
        print(f"{num} is not a perfect cube")

    user_choice=input("Do you want to continue? (yes/no): ").strip().lower()
    if user_choice=="no" or user_choice=="n":
        print("goodbye")
        break
    