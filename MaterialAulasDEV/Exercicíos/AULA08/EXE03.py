#CADASTRO, CALCULO DA MÉDIA, NOTAS ACIMA DA MÉDIA
nota = [""]*5
for i in range(len(nota)):
   nota[i] = float(input("Digite as notas da turma: "))
soma= 0
for j in range(len(nota)):
    soma = soma + nota[j]
media = soma/5
contador=0
for s in range(len(nota)):
    if nota[s]>media:
        contador=contador+1
print(f"{contador} notas são maiores que a média {media}")


