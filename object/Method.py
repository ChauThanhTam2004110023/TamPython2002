####@@@ Đóng gói
class Method:
    def __init__(self, tenxe, mau, nhienlieu):
        self.tenxe = tenxe
        self.mau = mau
        self = nhienlieu
        
    def dungxe(self, mucdich):
        return "{} đang dừng để {}" .format(self.tenxe, mucdich)
    def nomay(self, mucdich):
        return "{} đang {}" .format(self.tenxe, mucdich)
    def chayxe(self, mucdich):
        return "{} đang chạy {}" .format(self.tenxe, mucdich)

###Khởi tạo
toyota = Method("toyota", "trắng", "điện")
honda = Method("honda", "bạc xám", "xăng")
suzuki = Method("suzuki", "đen", "dầu")

###các phương thức
print(toyota.dungxe("nạp điện"))
print(honda.nomay("nổ máy xe"))
print(suzuki.chayxe("trên cao tốc"))