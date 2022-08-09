###@@@ Tuple
# được giới hạn bởi cặp ngoặc ()
# các phần tử của tuple được phân cách bởi dấu phẩy (,)
# Tuple có khả năng chứa mọi giá trị 
# tốc độ truy xuất của Tuple nhanh hơn list 
# dung lượng chiếm trong bộ nhớ nhỏ hơn list
# bảo vệ dữ liệu của bạn không bị thay đổi
# có thể dùng làm key của dictionnary #

tup = (i for i in range(10) if i%3 == 0)
a = tuple(tup)
print(a)

### Tạo một chuỗi liên kết
tup = (1,5,9)
tup += (2,4,6)
print(tup)
#or tup = (1,5,9)
# a += (2,4,6)
# print(a) #

tup = (2,4,6)
tup *= 5
print(tup)

##Truy xuất phàn tử đầu
tup = (1,2,3)
a = 1 in tup
print(a)

##Lấy phần tử trong chuỗi
tup = (1,5,9)
a = tup[1]
print(a)

##Kiểm tra cos bao nhiêu phần tử
tup = (1,5,7,9)
a = len(tup)
print(a)

##Truy xuất đến phần tử cuối
tup = (1,5,7,9)
a = tup[-1]
print(a)

##Truy xuất phần tử ngược lại
tup = (1,5,7,9)
a = tup[::-1]
print(a)

##Truy xuất xem vị trí phần tử bao nhiêu lần
tup = (1,5,5,7,9,1,5)
a = tup.count(5)
print(a)

