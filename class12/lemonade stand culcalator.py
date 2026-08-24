# lemon stand culcalator

def greet():
    print("welcome to lemonade stand")
    print("fresh lemonade mad just for you")

def calculateprice(price,cup):
    total = price * cup
    return total
def thankyou (cup):
    if cup >=5:
        print("wow! a big order thank you for the support")  
    else:
        print("thank you for atopping by the stand")

price = float(input("enter the price of lemonade : "))
cups = float(input("enter the no of cups : "))
print("**********************************************************")
greet()
totalprice = calculateprice (price,cups)
print("the price per cups is ",price)
print("the no. of cups is ",cups)
print("the total price is ",round(totalprice,2))
thankyou(cups)
print("*********************************************************")
