## Vòng lặp For

n = 10
for i in range(n):
    print(i)

#n = int(input("Nhập n vào: "))
##tong = 0
#for i in range(n+1):
#    tong += i
#print("Tổng: ", tong)

color = ["red", "green", "yello"]
for i in range(len(color)):
    print(color[i])

# or
color = ["red", "green", "yello"]
for color in color:
    print(color)


## VÒng lặp lồng nhau
for j in range(1,11):
    print("Bang cưu chương", j)
    for i in range(1,11):
        print("{0} x {1} = {2}" .format(i,j, j*i))