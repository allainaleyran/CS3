'''
Leyran, Allaina Maxene C.
9-Balingkilat

'''
class Glassware:
    def __init__(self, material):
        self.material = material
        
class Beaker(Glassware):
    def __init__(self, material, capacity):
        self.capacity = capacity
        super().__init__(material)
        
class Tray:
    def __init__(self):
        self.beakers = [Beaker("Glass", 100), Beaker("Glass", 200), Beaker("Glass", 300), Beaker("Glass", 400), Beaker("Glass", 500)]
        
Lab_tray = Tray()
print(len(Lab_tray.beakers))
