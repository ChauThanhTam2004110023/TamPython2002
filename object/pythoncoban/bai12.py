###@@@ Giải phương trình bậc 2

import math

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))
print("{0}x^2 + {1}x + {2} = 0" .format(a,b,c))

if(a != 0):
    delta = b**2 - 4*a*c
    if(delta < 0):
        print("Phương trình vô nghiệm")
    elif(delta == 0):
        x = -b/(2*a)
        print("Phương trình có nghiệm kép x1 = x2 = ", x)
    else:
        x1 = (-b-math.sqrt(delta)) / (2*a)
        x2 = (-b+math.sqrt(delta)) / (2*a)
        print("Phương trình có nghiệm phân biệt x1 = {0} và x2 = {1}" .format(x1, x2))
else:
    print("Không phải phương trình bậc 2")
