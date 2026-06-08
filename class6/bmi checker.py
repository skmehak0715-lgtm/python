# bmi hecker

w = float(input("enter the weight in kgs :"))
h= float(input("enter the hieght in m :"))

bmi = w/(h * h)
print("the bmi is",bmi)
if bmi < 18.5:
     print("you are underweight")
elif bmi < 25:
     print("you are healthhy")
elif bmi < 30:
     print("yuo are overweight")
else:
     print("you are obese")