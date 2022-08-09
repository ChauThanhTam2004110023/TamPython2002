'''Đối tượng: Object
Cách xác định địa chỉ của đối tượng bằng hàm id()
    1. Một đối tượng có cùng một địa chỉ là duy nhất
    2. Một đối tượng chứa bên trong đối tượng khác '''

class B5:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Hello(self):
        print(self.name+ " helloWord, i'm " +self.age)

p1 = B5("Chau Tam", "20")
p1.Hello()
