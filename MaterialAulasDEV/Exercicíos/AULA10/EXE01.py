nomes=[]
for i in range(2):
    nome = input("Digite 5 nomes: ")
    nomes.append(nome)
for nome in nomes:
    if nome[0] == "a" or nome[0] == "A":
        print (nome)
    else:
        print("esse nome não começa com a letra A")