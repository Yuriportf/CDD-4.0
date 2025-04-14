nota1 = float(input("Digite a nota 1: "))
while nota1 <0 or nota1 >10:
    nota1 = float(input("Digite a nota 1 novamente: "))
nota2 = float(input("Digite a nota 2: "))
while nota2 <0 or nota2 >10:
    nota2 = float(input("Digite a nota 2 novamente: "))
media = (nota1+nota2)/2
print(media)