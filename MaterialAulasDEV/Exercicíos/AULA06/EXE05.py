senha= 123456
i = 1
senhalo=int(input("Digite a senha: "))
while i <= 3 and senha != senhalo:
    senhalo = int(input("Digite a senha: "))
    i += 1
    #print("senha bloqueada")
if senhalo == senha:
 print("Seja bem vindo")


