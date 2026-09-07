import random


ch = ["rock","paper","scissors"]
while True:
    comp = random.choice(ch)
    user = input("enter rock or paper or sissors")
    print(comp)
    if comp.lower() == user.lower():
        print("it is a tie")
    elif (user.lower() == 'rock' and comp.lower() =='scissors') or (user.lower() == 'scissors' and comp.lower() =='paper') or(user.lower() == 'paper' and comp.lower() =='rock'):
        print("you win the game")

    else:
        print("computer wins")
    choice = input("do you want to play again (y/n)")
    if choice.lower() == "n":
        break
