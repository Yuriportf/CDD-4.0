resposta = "sim"
while resposta =="sim":
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite o sua altura: "))
    IMC = peso/altura**2
    if IMC < 18.6:
        print("Abaixo do peso")
    elif IMC >= 18.6 or IMC <= 24.9:
        print("Peso ideal PARABÉNS ")
    elif IMC >= 25.0 or IMC <= 29.9:
        print("levemente acima do peso")
    elif IMC >= 30.0 or IMC <= 34.9:
        print("Obesidade grau I")
    elif IMC >= 35.0 or IMC <= 39.9:
        print("Obesidade grau II (SEVERA)")
    else:
        print(" OBESIDADE GRAU III (MORBIDA)")
    resposta = input(f"Deseja contar o IMC novamente ?")


