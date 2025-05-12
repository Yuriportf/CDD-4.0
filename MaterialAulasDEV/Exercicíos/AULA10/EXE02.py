lista = 20
contador=0
while contador < 101:
    chute = int(input("Digite o seu número: "))
    if chute <lista:
        print("Esse número é menor que o número oculto")
    elif chute >lista:
        print("Esse número é maior que o número oculto")
    else:
        print("Parabéns você acertou!!!! ")
