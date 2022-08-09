class List:
    #### Contructor(hàm)
    def __init__(self, hangxe, tenxe):
        self.hangxe = hangxe
        self.tenxe = tenxe
        
    #### Method(phương thức)
    def chayxe(self):
        print("{} đang chạy" .format(self.tenxe))
    def dungxe(self, mucdich):
        print("{} đang dừng xe {}" .format(self.tenxe, mucdich))

class toyota(List):
    def __init__(self, hangxe, tenxe, nhienlieu):
        super().__init__(hangxe, tenxe)
        self.nhienlieu = nhienlieu
    
    def chayxe(self, mucdich):
        print("{} đang chạy {}" .format(self.tenxe, mucdich))
    def dungxe(self, mucdich):
        print("{} đang dừng xe để {} {}" .format(self.tenxe, mucdich, self.nhienlieu))
    def nomay(self, mucdich):
        print("{} đang nổ máy {}" .format(self.tenxe, mucdich))
    
class Honda(toyota, List):
    def __init__(self, hangxe, tenxe, nhienlieu):
        super().__init__(hangxe, tenxe, nhienlieu)

    def suaxe(self, mucdich):
        print("{} dang {}" .format(self.tenxe, mucdich)) 
    def dichuyen(self, mucdich):
        print("{} dang {}" .format(self.tenxe, mucdich))
    
