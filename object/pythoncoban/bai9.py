###@@@cac toan tu so sanh va logic 
print("Tra ve true vs false")
a = int(input("a: "))
b = int(input("b: "))

print("{0} > {1} la: {2}" .format(a,b, a > b))
print("{0} < {1} la: {2}" .format(a,b, a < b))
print("{0} == {1} la; {2}" .format(a,b, a == b))
print("{0} >= {1} la: {2}" .format(a,b, a >= b))
print("{0} <= {1} la: {2}" .format(a,b, a <= b))
print("{0} != {1} la: {2}" .format(a,b, a != b))

print("Toan logic")
d = int(input("d: "))

print("({0} < {1}) and ({2} < {3}) = {4}" .format(a,b,b,d, (a>b) and (b<d)))
print("({0} < {1}) or ({2} > {3}) = {4}" .format(a,b,b,d, (a<b) or (b>d)))
print("not ({0} > {1}) = {2}" .format(a,b,not (a>b)))

