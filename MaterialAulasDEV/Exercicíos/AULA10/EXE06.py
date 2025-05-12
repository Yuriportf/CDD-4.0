soma=0
for i in range(5):
    numeros = int(input("Digite um número: "))
    soma=numeros + soma
media=soma/5
print(media)
if media > 7 and media <=10:
    print("Aluno aprovado")
elif media < 4:
    print("Aluno reprovado")
elif media >= 4 and  media < 7:
    print("Aluno em recuperação")
elif media > 10:
    print ("valor inválido")
elif media < 0:
    print("valor inválido")
else:
    pass