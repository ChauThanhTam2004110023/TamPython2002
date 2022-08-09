a = "\n howkteam"
b = a*10
print(b)

chuoi_1 = "Xin chao TITV"
chuoi_2 = "TITV"
chuoi_3 = "Xin chao"
if chuoi_2 in chuoi_1:
    print("CHuỗi 1 là con chuỗi 2")
else:
    print("Chuỗi 2 không là con của chuỗi 1")

if chuoi_3 in chuoi_1:
    print("Chuỗi 3 là con chuỗi 1")
else:
    print("Chuỗi 3 không là con chuỗi 1")

## hoa hữ cái đầu
s = "howkteam"
s = str.capitalize(s)
print(s)
#hoa toan bộ
s = str.upper(s)
print(s)
#thường toàn chuỗi
s = str.lower(s)
print(s)
##tìm và đếm số lượng
s = "lập trình python là xu thế hiện tại"
print(s.find("tại"))

## tách chuỗi
s = "lặp trình Python là xu thế. Bạn nên học lặp trình Python"
list = s.split("  ")
print(list)

print("{0} + {1} = {2} " .format(1,2, 1+2))
