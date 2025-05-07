class Animal ():
    def __init__(self,nome,age,peso):
       self.nome=nome
       self.peso=peso
       self.idade=age
       self.Comer= False
       self.Dormir= False
    def Apresentar (self):
         print(f"Olá, eu sou {self.nome} eu tenho {self.idade} e eu peso {self.peso}")
    def Comer(self):
        if  self.Dormir() == False:
            return self.comer() True
            return ("Eu estou Comendo")
    def Dormir(self):
        if self.Comer() == False:
            return self.Dormir()True
        elif self.Dormir() == True
            return("Eu estou dormindo")

