x = 5
print(id(x))
del(x)

### Xóa theo vi trí trong chuỗi
myList = ['red', 'blue', 'yello', 'black']
print(myList)
del myList[1:2]
print(myList)

myList = ['blue', 'yello', 'red', 'black', "queen", 'king']
print(myList)
myList.remove('red')
print(myList)

### Xóa toàn bộ trong chuỗi
myList = ['blue', 'yello', 'red', 'black', "queen", 'king']
print(myList)
myList.clear()
print(myList)

### Xóa phần tử trùng trong chuỗi
myList = ['red', 'blue', 'yello', 'black', 'blue', 'black']
print(myList)
unique_list = list(set(myList))
print(unique_list)

### Xóa phần tử số lẻ theo điều kiện
myList = list(range(10))
print(myList)
xoa_so_le = [num for num in  myList if num % 2 == 0]
print(xoa_so_le)

### Xóa phần tử số chẵn theo điều kiện
myList = list(range(10))
print(myList)
xoa_so_chan = [num for num in myList if num % 2 == 1]
print(xoa_so_chan)


