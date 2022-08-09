
class Inheritance1:
    def __init__(self):
        print("Lop cha")

    def WhoisThis(self):
        print("Lop")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Inheritance1):
    def __init__(self):
        super().__init__()
        print("Inheritace is ready")

    def WhoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.WhoisThis()
peggy.swim()
peggy.run()
