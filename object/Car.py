class Car:
    def __init__(self, tenxe, mausac, soluong):
        self.tenxe = tenxe
        self.mausac = mausac
        self.soluong = soluong

    def show(self):
        print(f"tên xe: {self.tenxe}")
        print(f"màu sắc: {self.mausac}")
        print(f"số lượng: {self.soluong}")

### testdrive
car = Car("toyota", "Bạc Xám", 20)
car.show()
car1 = Car("suzuki", "Trắng", 40)
car1.show()