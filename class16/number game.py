# NUMBER GAME

import random

computer = random.randint (1,100)

while True:
    n = int(input("enter a number : "))
    if n == computer:
        print("you win ")
        break
    elif n > computer:
        print("the number ginen is greater")
    else:
        print("the number glven is smaller")