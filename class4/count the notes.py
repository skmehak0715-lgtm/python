#count the notes

amt = int(input("enter the amt : "))
note500 = amt//500
note100 = (amt%500)//100
note50 = ((amt%500)%100)//50

print("the number of 500 rupee note : ",note500)
print("the number of 100 rupee note : ",note100)
print("the number of 50 rupee note : ",note50)