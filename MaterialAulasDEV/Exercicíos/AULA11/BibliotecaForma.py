class Forma():
    def __init__(self):
        self.area=0
        self.perimetro=0

class Triangulo(Forma):
    def __init__(self,altura,base):
        self.base=base
        self.altura=altura
        super().__init__()
    def calcularArea(self):
       self.area = (self.area*self.altura)/2
       print(self.area)
    def calcularPerimetro(self):
       self.perimetro = (self.base*3)
       print(self.perimetro)

class Retangulo(Forma):
    def __init__(self,altura,base):
        self.base=base
        self.altura=altura
        super().__init__()
    def calcularArea(self):
       self.area = (self.area*self.altura)/2
       print(self.area)
    def calcularPerimetro(self):
       self.perimetro = 2 * (self.base+self.altura)
       print(self.perimetro)