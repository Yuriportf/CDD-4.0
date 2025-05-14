class ingresso ():
    def __init__(self,valor):
        self.valor = valor
    def imprimirValor(self):
        print(f"o valor é de R$ {self.valor}")

class vip (ingresso):
    def __init__(self,valor):
        super().__init__(valor*1.5)


