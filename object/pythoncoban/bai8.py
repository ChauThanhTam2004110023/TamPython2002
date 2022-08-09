
a = "How kteam free education"
b = a.split(" ", 2)
print(a)
print(b)

a = "How kteam free education"
b = a.rsplit(" ", 1)
print(a)
print(b)

###kiem tra co bao nhieu ky tu k
a = "how kteam free education"
b = a.startswith("k", 5)
print(a)
print(b)

###tim kiem ky tu tu trai qua
a = "how kteam free education"
b = a.rfind("n")
print(a)
print(b)

###tim kiem ky tu phai qua
a = "how kteam free education"
b = a.find("h")
print(a)
print(b)

###tim kiem ki tu viet hoa toan bo
a = "HOW KTEAM FREE EDUCATION"
b = a.isupper()
print(a)
print(b)

###tim kiem ki tu viec so toan bo
a = "12333456678"
b = a.isdigit()
print(a)
print(b)

###tim kiem co khoang trang không
a = " "
b = a.isspace()
print(a)
print(b)
print()

###Nhập 
a = str(input("A: "))
print(a.isdigit())