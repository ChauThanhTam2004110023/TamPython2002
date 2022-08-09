## kiem tra chuoi 
s = "abcd"
x = s.isalpha()
print(x)

## tra ve True -> chi chu so 0,1,2,..9 ko chap nhan ky tu
s = "1467234"
x = s.isdecimal()
print(x)

## tra ve True -> chi chu so 0,1,2,..9 ko chap nhan ky tu
s = "1097234h"
x = s.isdigit()
print(x)

## isnumerric
## so vs ky tu
s = "abcd12435"
x = s.isalnum()
print(x)

## tra ve false khi co chu viet hoa
s = "123456abcd"
x = s.islower()
print(x)

### tra ve false khi co chu viet thuong
s = "123@ASDCF"
x = s.isupper()
print(x)

s = "Lap Trinh Python"
x = s.istitle()
print(x)