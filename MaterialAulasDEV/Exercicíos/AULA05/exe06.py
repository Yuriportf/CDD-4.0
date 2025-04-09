som = 0
fora = 0
for i in range(1,11,1):
    num = int(input("Digite seus números de 10 a 20: "))
    if num >= 10 and num <= 20:
        som= som+1
    else:
        fora= fora+1
print(f"os valores no intervalo são {som} e valores fora do intervalo {fora}")
