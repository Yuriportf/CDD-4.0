"""ArraysCompras = ["banana","laranja","maçã"]
for i in ArraysCompras:
    print(i)"""

"""for i in("banana","laranja","maçã"):
    print(i)"""

"""frutas=["banana","laranja","maçã"]
for i in range(len(frutas)):
    print(frutas[i], end=",")"""



alunos=[""]*5
for i in range(len(alunos)):
    alunos[i]=input("Digite um nome: ")
    ind=len(alunos)
print(alunos, ind)
for j in range(len(alunos)):
    print(alunos[j],j)