print("consulte a sua média anual !!!!")
aluno=input("Digite o seu nome: ")
nota1=float(input("Digite a sua primeira nota semestre: "))
nota2=float(input("Digite a sua segunda nota do semestre: "))
nota3=float(input("Digite a sua terceira nota do semestre: "))
media=(nota1+nota2+nota3)/3
if media >= 7:
    print(f"O aluno {aluno} foi a provado com a média {media:.2f} ao final do semestre")
elif media >= 4:
    print("o aluno está na recuperação final")
else:
    print(f"O aluno {aluno} foi a reprovado com a média {media:.2f} ao final do semestre")