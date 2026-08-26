# tip to the waiter
def tip(amt,per):
    tipamt = amt *per/100
    print("the bill amt is :",amt)
    print("the tip amt is :",tipamt)
    print("the total amt is :",amt + tipamt)

amt = float(input("enter the amout : "))
tip(amt,2)