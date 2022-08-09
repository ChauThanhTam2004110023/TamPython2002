
class Inherritance:
    stu = 0
    def __init__(self):
        self.name = input("Nhập tên: ")
        self.age = input("Nhập tuổi: ")
        Inherritance.stu += 1
    def display(self):
        print("Tên: ", self.name, "age: ", self.age)

In1 = Inherritance()
In2 = Inherritance()
In1.display()
In2.display()
print("input: ", Inherritance.stu)
        
    
        

