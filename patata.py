class patata:
    def __init__(self, name='', size=0.0, farms=[]):
        self.name = name
        self.size = size
        self.farms = farms
    def __repr__(self):
        return "name: " + self.name.__repr__() + "\n" + \
               "size: " + self.size.__repr__() + "\n" + \
               "farms: " + self.farms.__repr__()
