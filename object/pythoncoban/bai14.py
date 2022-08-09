####@@@ Kieu du lieu List
### Các phần tử của list cách nhau bởi dấu phẩy
#### Tạo ra một x từ 0 -> 30(tạo 30 phần tử bắt đầu từ 0)
a = [kteam for kteam in range(30)]
print(a)

b = [[n, n*1, n*2] for n in range(1,4)]
print(b)

a = ["kteam"]
#a = a + ["one", "two"] liên kết a vs nhau
# a *= 2 nhân đôi
b = "kteam" in a #Kiểm tra xem có trong chuỗi ko
print(b)

## Lấy một giá trị theo thứ tự, rồi thêm giá trị mới vào
a = [1,2, "a", "b", "c", [3,4]]
a[1] = "kteam"
b = a[1]
print(a)
print(b)

### Ma Trận
a = [[1,2,3], [4,5,6], [7,8,9]]
print(a[0])
print(a[1])
print(a[2])
print()

##@@@@
a = [1,2,3]
b = list(a)
print(a)
print(b)
b[0] = "kteam"
print(a)
print(b)
print()

####@@@@
a = [[1,2,3], [4,5,6]]
b = list(a)
print(a)
print(b)
b[0] = "kteam"
print(a)
print(b)

s = [input("nhập: ") for i in range(3)]
print(s)

