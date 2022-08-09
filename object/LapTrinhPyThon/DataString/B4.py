## tìm xem nó xuất hiện bao nhiêu lần => xuất hiện 2 lần
from calendar import c
from pickle import TRUE

### tìm xem vó bao nhiêu phân tử trùng nhau
s = "nss channerl nss"
z = s.count("nss")
print(z)

s = [1,2,3,4,5]
z = s.count(1)
print(z)

## vị trí ở thứ mấy => 9
s = "nss chanel"
z = s.index("l")
print(z)

s = ['Lap trinh python']
z = s.copy()
z.append("Hello")
print(z)

## xoa het cac phan tu trong chuoi
s = ["lap trinh python"]
z = s.clear()
print(z)

## bo mot phan tu bat ky
s = [1,22,3,4,55]
z = s.pop(2)
print(s)

##đảo ngược
s = [1,2,3,4,5,6,7]
s.reverse()
print(s)

## tăng dần
s = [9,5,7,1,33,3,4,2,8,10]
s.sort(reverse=False)
print(s)

## giảm dần
s = [9,5,7,1,33,3,4,2,8,10]
s.sort(reverse=True)
print(s)

