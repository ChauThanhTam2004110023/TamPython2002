###@@@ Toán tử điều kiện
x = float(input("a: "))
x = int(x)

kp = "Chẵn" if(x%2 == 0) else "lẻ"
print(x, "là số ", kp)

###@@@ Toán tử điều kiện IF and ELSE
x = input("Nhập một số nguyên: ")
x = int(x)

if x > 0:
    print(x, "là số dương")
else:
    print(x, "là số âm")


###@@@ IF ang ELSE
x = input("Nhập điểm: ")
x = int(x)

if(x >= 9):
    print("Xuất sắc")
elif(x >= 8):
    print("Giỏi")
elif(x >= 7):
    print("Khá")
elif(x >= 6):
    print("Trung bình")
else:
    print("Yếu")