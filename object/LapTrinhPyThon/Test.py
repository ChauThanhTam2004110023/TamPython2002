# str = "\n Le Hoang Thach"
# str1 = str * 20
# print(str1)

#class Test:
#    name = "Lap Trinh Python"

#    def __repr__(self):
#        return repr("Xin Chao " +self.name)
#print(repr(Test()))

#rint(chr(-1))

class Test:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age

