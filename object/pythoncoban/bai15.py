### Kiểu dữ liệu List
# Count: đếm
a = [1,1,1,2,2,3,4,5,6,7,8]
c = a.count(1)
print(c)

## vị trí
a = [1,1,1,2,2,3,4,5,6,7,8]
c = a.index(1)
print(c)

## tạo ra một bản sao
a = [1,1,1,2,2,3,4,5,6,7,8]
c = a.copy()
c[0] = "kteam"
print(c)

## Xóa các phần tử có trong list
a = [1,1,1,2,2,3,4,5,6,7,8]
c = a.clear()
print(a)
print(c)

##
tien_teo = [50]
tien_cua_gau_teo = tien_teo
print(tien_teo)
print(tien_cua_gau_teo)

tien_cua_gau_teo.clear()
print(tien_teo)
print(tien_cua_gau_teo)

## thêm
a = [1,2,3,4]
a.append([4,5])
print(a)

## Mở rộng 
a = [1,2,3]
a.extend([4,5, [7,8]])
print(a)

## Thêm phần tử vào vị trí i
a = [1,2,3]
a.insert(0,4)
print(a)

## bỏ đi phần tử thứ i
a = [1,2,3]
c = a.pop(1)
print(c)
print(a)

## bỏ đi phần tử đầu tiên trong list
a = [1,2,3]
a.remove(1)
print(a)

## list đảo ngược
a = [1,2,3,4]
a.reverse()
print(a)

## tự sắp xếp tăng dần or giảm dần
a = [9,8,7,6,5,4,3,2,1]
a.sort(reverse=False)
print(a)