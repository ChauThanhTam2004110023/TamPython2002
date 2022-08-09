class School:
    #def __init__(self):
    #    self.ten = " "
    #    self.tuoi = " "
    #    self.gioitinh = " "
    #    self.email = " "
        
    #def print(self):
    #    self.name = input("Ten: ")
    #    self.tuoi = input("Tuoi: ")
    #    self.gioitinh = input("Gioi tinh: ")
    #    self.email = input("Email: ")

    #def getPrint(self):
    #    print(self.name.title())
    #    print(self.tuoi.title())
    #    print(self.gioitinh.title())
    #    print(self.email.title())
    def __init__(self, name, age, email):
        self.__name = name
        self.__age = age
        self.__email = email
    def get__name(self):
        return self.__name
    def get__age(self):
        return self.__age
    def get__email(self):
        return self.__email
    
    def print(self):
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.email = input("Email: ")
    def getPrint(self):
        print(self.name.title())
        print(self.age.title())
        print(self.email.title())

    


        