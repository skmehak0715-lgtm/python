mc =      input("does the student have a medical] cause (y/n) : ")
if mc.lower() == 'n':
    att = int(input("enter the attendance :"))
    if att > 75:
        print("the student is allowed to write the exam")
    else:
         print("the student is allowed to write the exam")
else:
     print("the student is allowed to write the exam")