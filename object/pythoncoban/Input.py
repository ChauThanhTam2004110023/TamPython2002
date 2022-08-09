
''''a = int(input("Input: "))

if a == 2:
    print("Thứ hai")
elif a == 3:
    print("Thứ ba")
elif a == 4:
    print("Thứ tư")
elif a == 5:
    print("Thứ năm")
elif a == 6:
    print("Thứ sáu")

b = [input("Nhập: ") for i in range(4)]
print(b)

c = int(input("Nhập số: "))
if c > 0:
    print(c, "là số dương")
else:
    print(c, "là số âm")'''

c = str(input("nhập: "))
print(c.isdigit())