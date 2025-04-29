NOMES = ["JOÃO","CARLOS","MARIA","LUIZA","ISABEL"]
NOMESA = input("Digeirte um nome: ")
for i in range(len(NOMES)):
    if NOMESA == NOMES[i]:
        print(f"O nome encontrado foi {NOMESA} NA POSIÇÃO {i}")
        break
    else:
        print("nome não encontrado")


N