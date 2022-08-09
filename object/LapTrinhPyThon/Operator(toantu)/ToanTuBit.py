''' TOÁN TỬ THAO TÁC BIT
    and bit: &       x = 5 & 3
    or bit: |       x = 5 | 3
    xor bit: ^      x = 5 ^ 3
    Dịch trái: <<   x = y << 2
    Dịch phải: >>   x = y >> 2'''


from re import X


x = 4 & 2 # & : giao 
# "0000 0101" ## chuyển 5 sang nhị phân
# "0000 0011" ## chuyển 3 sang nhị phân
# "0000 0001" ## -> 1 giao

print(x)

y = 5 | 3 #|: hop
#"0000 0101" ## chuyển 5 sang nhị phân
#"0000 0011" ## chuyển 3 sang nhị phân
#"0000 0111" ## -> 7 
print(y)
# '''4 & 2
# 0000 0100 4 sang nhị phân
# 0000 0010 2 sang nhị phân
# 0000 0000 -> 4''' 

# print(y)

###@@ Chuyển thập phân sang nhị phân
#n = -1
#while(n <= 0):
#    n = int(input("Nhập: "))
#@ Chuyển thập phân sang nhị phân
#x = n
#ketQua = " "
#while(n>0):
#    ketQua = str(n%2)+ketQua
#    print("n%2: ", n%2)
#    n = n//2
#    print("n: ", n)
#print("kết quả: ", ketQua)
