numero = int(input("Digite seu número: "))
if numero % 1  and numero > 0:
    print(f"O número é impar e positivo {numero}")
elif numero % 1 and numero < 0:
    print(f"O número é impar e negativo {numero}")
elif numero % 2 and numero < 0:
    print(f"O número é impar e negativo {numero}")
else:
    print(f"O número é par e positivo {numero}")



