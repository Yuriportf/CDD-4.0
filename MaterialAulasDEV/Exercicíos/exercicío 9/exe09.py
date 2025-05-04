usuarios = ["joao", "carlos", "mario", "maria", "josefa"]
senhas = [1234, 3432, 5432, 3333, 6666]

login = input("Digite seu nome de usuário: ")
senha = int(input("Digite sua senha: "))

for i in range(len(usuarios)):
    if login == usuarios[i] and senha == senhas[i]:
        print(f"Bem-vindo, {login}! Login efetuado com sucesso.")
        break
else:
    print("Usuário ou senha incorretos.")
