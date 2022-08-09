from decimal import Decimal
from fractions import Fraction


x = 23
y = 33
z = Decimal(x)+Decimal(y)
print(z)  
print(type(z))

y = Decimal("0.05") + Decimal("0.05")
print(y)

z = Decimal(0.05) + Decimal(0.05)
print(z)

###@@ Phân số
x = Fraction(2,3)
y = Fraction(2,3)
z = x + y
print(z)
print(type(z))

x = 3 + 2j
y = 3 + 2j
z = x + y
print(z)
print(z.imag)
print(type(z))


x = str(input("Nhap: "))
y = str(input("Nhap: "))
z= (Fraction(x) + Fraction(y))
print(z)

a = str(input("a: "))
b = str(input("b: "))
c = (Decimal(a) + Decimal(b))
print(c)