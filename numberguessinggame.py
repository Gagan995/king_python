import random

number=random.randint(1,10)
attempt =0

while attempt:
     
    user_guess=int(input("Gues the numnber between 1 to 10"))

    if user_guess > 10 or user_guess < 0:
        print("Please Enter the void number")
    if (number==user_guess):
        print("congrats you win!!!!!!")
        break
    elif (user_guess<number):
        print("your guess is low, please guess the higher number")
    else:
        print("please guess is high, please guess the lower number")