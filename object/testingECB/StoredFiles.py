import json


class StoredFiles:
    def __init__(self, filename):
        self.stored_file = filename
        self.memory = self.read()
    
    def read(self):
        afile = open(self.stored_file, "r")
        return json.load(afile)
    
    def get_all(self):
        return self.memory
    
    def update(self, **kwargs):
        self.memory.append(kwargs)

    def write(self):
        with open(self.stored_file, "w") as afile:
            json.dump(self.memory,afile)


    def search(self, key, val):
        idx = -1
        for elem in self.memory:
            if elem[key] == val:
                idx = self.memory.index(elem)
                return idx
        return idx

