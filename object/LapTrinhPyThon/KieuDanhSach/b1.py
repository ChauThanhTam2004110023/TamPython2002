from re import X


y = ("m", "n", 1,2,3,4)
x = [4,5,6,7,8, y]
print(x)

## lay danh sach ơ vi tri thu
z = x[5][0] ## [5:0]
print("z= " , z)
print("x = ", x)

## ktra trong danh sach co bao nhieu phan tu
y = [1,2,3,4,5]
x = len(y)
print(x)

y = [1,2,3,4,5]
x = min(y)
print(x)


a = ["a", "b", 1,2,3,9,6,0]
b = (1,4,6,2,3, a)
print(b)
c = len(b)
print(c)



