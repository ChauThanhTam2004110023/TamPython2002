##tạo 2 method
##có input

#class Test:
#    def __init__(self):
#        self.name = " "
#        self.age = " "

#    def getString(self):
#        self.name = input("Name: ")
#        self.age = input("Age:")

#    def printString(self):
#        print(self.name.title())
#        print(self.age.title())

#strObj = Test()
#strObj.getString()
#strObj.printString()

##@ kế thừa đơn
##class Test:
#   def speak(self):
#        print("Animal Speaking")
    
#class Animal(Test):
#    def bark(self):
#        print("Quào Quào")
#d = Animal()
#d.speak()
#d.bark()

##@ kế thừa đa cấp bật
#class Test:
#    def Animal(self):
#        print("Speaking animal")
#class Dog(Test):
#    def Dog(self):
#        print("Quao Quao")
#class Cat(Dog):
#    def Cat(self):
#        print("Meo Meo")

#d = Cat()
#d.Animal()
#d.Dog()
#d.Cat()

class Test:
    def __init__(self, tenxe, nhienlieu):
        self.tenxe = tenxe
        self.nhienlieu = nhienlieu
    def chayxe(self):
        print("{} dang chay ".format(self.tenxe))
    def dungxe(self, mucdich):
        print("{} dang {}".format(self.tenxe, mucdich))

class TestDrive(Test):
    def __init__(self,tenxe, nhienlieu):
        super().__init__(tenxe, nhienlieu)
        self.nhienlieu = nhienlieu

    def chayxe(self, mucdich):
        print("{} chay bang {} dang di chuyen {} " .format(self.tenxe,self.nhienlieu, mucdich))
    def dungxe(self, mucdich):
        print("{} dung lai de {} {} " .format(self.tenxe, mucdich, self.nhienlieu))
    def nomay(self, mucdich):
        print("{} dang {} {}" .format(self.tenxe,mucdich, self.nhienlieu))

TestDrive1 = TestDrive("Toyota Lan Cruiser", "Xang")
TestDrive2 = TestDrive("Honda Vuirut", "Dau")
TestDrive3 = TestDrive("Vinfact Lax 2.0", "Dien")

TestDrive1.chayxe("Tren cao toc")
TestDrive2.dungxe("Nap nhien lieu")
TestDrive1.dungxe("nap nhien lieu ")
TestDrive3.nomay("Cho doi ngyeu va sac")
