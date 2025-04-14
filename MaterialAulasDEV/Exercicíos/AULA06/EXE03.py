i = 1
media=0
soma=0
quantidade=int(input("Digite a quantidade de alunos: "))
while i <= quantidade:
    notas=int(input("Digite as notas dos alunos: "))
    soma = notas + soma
    i += 1
media = soma/quantidade
print(media)