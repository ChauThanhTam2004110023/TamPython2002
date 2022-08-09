## noi giua cac chuoi lai voi nhau
s = "------------"
z = ["Hello", "Lap trinh python", "2022"]
y = s.join(z)
print(y)

## do dai cua ky tu
s = "lap trinh python"
z = len(s)
print(z)

## thay the cu thanh moi: nss la ky tu can thay, MMM la ky tu moi, 2 la so ky tu thay
s = "nss channel, nss channel, nss channel, nss channel"
z = s.replace("channel","MMM", 2)
print(z)

## loai bo (-): ky tu can loai bo
s = "-----nss channel--------"
z = s.strip("-")
print(s)
print(z)

## bo ky tu ben trai
s = "---------nss channel---------"
z = s.lstrip("-")
print(z)

## bo ky tu ben phai
s = "---------nss channel---------"
z = s.rstrip("-")
print(z)

s = input("Nhap: ")
print(s.rstrip("-"))

s = input("Nhap: ")
print(len(s))