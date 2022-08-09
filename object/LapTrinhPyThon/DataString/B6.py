s = "Lap trinh python"
z = s.split(" ")
print(z)

## tao phan tu trong mot danh sach
s = """Lap trinh python
Hello Word"""
z = s.splitlines(False)
print(z)

## dien day ky tu 0 vao ben trai cho vua du
s = "Lap trinh python"
z = s.zfill(50)
print(z)

## mo rong (\t)
s = "Lap \t trinh \t python"
z = s.expandtabs(10)
print(s)

## ma hoa chuoi s(8,16,32.....) encode: ma hoa, decode: giai ma
s = "Lap trinh python"
z = s.encode("utf-16")
y = z.decode("utf-16")
print(z)
print(y)

## max tra ve vi tri lon nhat
## min tra ve vi tri nho nhat
## ky tu(chu) tra bang ma ASCII
## bang ma ASCII dung cho ca list, set, tuple
s = "ab"
z = max(s)
print(z)

s = [1,2,3,4,5]
z = max(s)
print(z)
#=> 5

###
s = "abcd"
z = min(s)
print(z)