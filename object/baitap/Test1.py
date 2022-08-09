## tạo 1 method
from cgi import test


class Test1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

test1 = Test1("ThanhTam", 20)
test1.show()
test1 = Test1("TamChau", 22)
test1.show()

