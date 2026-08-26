# cube of a cube
def cube(x):
    return x*x*x

def divisible_by_3(x):
    if x%3 == 0:
       return cube(x)
    else:
         return False

print("the cube of the number which is divisible by 3 :",divisible_by_3(27))
print("the number not divisble by 3",divisible_by_3(7))