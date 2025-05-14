class animal():
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor
    def comer(self):
        print(f"O {self.nome} foi comer")

class Gato(animal):
    def __init__ (self,nome,cor):
        super(). __init__(nome,cor)
    def miar(self):
        print(f" O {self.nome} foi miando...")

class Cobra(animal):
    def __init__(self,nome,cor):
        super(). __init__(nome,cor)
    def estrangular(self):
        print(f" A {self.nome} está estranculando...")

class vaco(animal):
    def __init__(self,nome,cor):
        super(). __init__(nome,cor)
    def mugir(self):
        print(f"O {self.nome} faz mooo....")


