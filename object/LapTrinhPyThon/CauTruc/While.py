# tien = 100
# while tien > 0:
#     print("Vẫn còn sài đc ", tien)
#     tien = tien - 10


k = 5
while k > 0:
    print('k: ', k)
    k -= 1

n = -1
while(n <= 0):
    n = int(input("nhap n: "))
i = 0
tong = 0
while (i <= n):
    tong = tong + i
    i += 1
print("Tong: ", tong)

j = 0
while(j <= 20):
    print(j, " Bên trong ")
    j += 1
    # if(j >= 5):
    #     break
else:
    print(j, " Bên ngoài ")
