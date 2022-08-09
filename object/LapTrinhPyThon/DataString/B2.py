"""chr(ascii) -> ob kieu str
repr(ob) -> ob kieu str

str(ob) -> ob kieu str
object thuoc lop str"""

s = 65
z = chr(s)
print(s)
print(type(s))
print(id(s))

print(z)
print(type(z))
print(id(z))


s = 12
z = repr(s)
print(s)
print(type(s))
print(id(s))

print(z)
print(type(z))
print(id(z))

s = [1,2,3, 'ac']
z = str(s)
print(s)
print(type(s))
print(id(s))

print(z)
print(type(z))
print(id(z))