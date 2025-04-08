compraquantidade=float(input("Digite a quantidade de litros compradas: "))
comprtipo= input("Digite o tipo: ")
E = 4.90
G =  5.80
if comprtipo == "E"or comprtipo =="e": #não pode só colocar o or tem q repetir a comparaçãp
    compraetanol = compraquantidade * E
    print(f"a compra de Etanol foi realizada no valor de {compraetanol}")
elif comprtipo == "G" or "g":
    Compragasolina = compraquantidade * G
    print(f"a compra de Gasolina foi realizada no valor de {Compragasolina}")
else:
    print("compra não realizada")



