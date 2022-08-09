## kiem tra xem mot chuoi co nam trong chuoi hay ko
from re import A


stra = "Howkteam.com"
strb = "K"
strc = strb in stra
print(strc)

## lay vi tri theo thu tu trong chuoi
stra = "Howkteam.com"
strb = stra[3]
strc = strb in stra
print(strc)

### lay ra do dai cua chuoi nam ben trong cap dau ngoac tron
stra = "Howkteam.e"
strb = stra[len(stra)- 1]
print(strb)

## cat chuoi
stra = "Howkteam"
strb = stra[1:5]
print(strb)
##None la vi tri bat dau
stra = "Howkteam"
strb = stra[1:None]
print(strb)

## ep kieu chuoi
stra = float(6.9) + 5
print(stra)

## chia het cho 2
a = [10, 9, 8, 7, 6, 1, 2, 3]
b = list(filter(lambda a: (a%2 == 0), a))
print(b)

## viet hoa ky tu dau chuoi 
a = "how kteam - free education"
b = a.capitalize()
print(b)

## viet hoa tat ca chuoi trong ngoac
a = "how kteam - free education"
b = a.upper()
print(b)

## hoa thanh thuong, thuong thanh hoa
a = "HOWKTEAM - FREE EDUCATION"
b = a.swapcase()
print(b)

### hoa chu cai dau

### canh phai vi tri cua chuoi
a = "kteam"
b = a.center(30)
print(b)
### canh trai ljust

## phuong thuc xu ly
## phuong thuc dung de encode(ma hoa kieu du lieu) mot chuoi
## Encode an, che giau thong tin du lieu
## Encode ma hoa de hien thi lai cac chu ko hien thi dc (VD: tieng latinh, tieng thai de ma hoa sang tieng viet)
a = "kteam"
b = a.encode(encoding="utf-8", errors="strict")
print(b)

###
a = "Những người học lạp trình"
b = a.encode()
print(a)
print(b)




