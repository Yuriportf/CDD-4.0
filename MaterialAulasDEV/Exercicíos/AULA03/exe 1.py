Pessoa_espec=input("Digite seu nome: ")
idade_pess=int(input("Digite a sua idade: "))
salario_pes=float(input("Digite o seu salário mensal: "))
PORFCENTAGEMDESEJADA=float(input("Digite a quantidade desejada: "))
almentoporc=float(salario_pes*PORFCENTAGEMDESEJADA)/100
salariofinal=almentoporc+salario_pes
print(f"{Pessoa_espec} tem {idade_pess} anos de idade e ganha {salario_pes} R$ mensalmente como progamador,\n",
f"Recentemente {Pessoa_espec} recebeu um almento de {almentoporc} R$ \n",
f"totalizando um porcentual de 20% sendo o salário almentado de {salariofinal} R$ \n")