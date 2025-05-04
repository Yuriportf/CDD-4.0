import random

animais = [
    "elefante", "girafa", "cachorro", "gato", "leão", "tigre", "lobo", "coelho",
    "jacaré", "papagaio", "águia", "tubarão", "golfinho", "baleia", "pinguim",
    "cavalo", "camaleão", "guaxinim", "coruja", "raposa",
    "antílope", "zebra", "rinoceronte", "hipopótamo", "tamanduá", "panda",
    "orangotango", "mico", "flamingo", "ganso", "urso", "cervo", "texugo",
    "cobra", "lagarto", "ema", "suricata", "canguru", "lhama", "quati"
]
animais = animais[:20]

palavraescolhida = random.choice(animais)

tentativasrestantes = 6
estagioforca = [
r'''
   _______
  |/      |
  |       
  |       
  |       
  |       
 _|___    
''',
r'''
   _______
  |/      |
  |      (_)
  |       
  |       
  |       
 _|___    
''',
r'''
   _______
  |/      |
  |      (_)
  |       |
  |       |
  |       
 _|___    
''',
r'''
   _______
  |/      |
  |      (_)
  |      \|
  |       |
  |       
 _|___    
''',
r'''
   _______
  |/      |
  |      (_)
  |      \|/
  |       |
  |       
 _|___    
''',
r'''
   _______
  |/      |
  |      (_)
  |      \|/
  |       |
  |      / 
 _|___    
''',
r'''
   _______
  |/      |
  |      (_)
  |      \|/
  |       |
  |      / \ 
 _|___   💀 Você Morreu! 💀
'''
]

# aqui esse vetor vai receber as letras acertadas durante o jogo.
descobertas = [""] * len(palavraescolhida)

print("Bem-vindo ao jogo da forca!")

while tentativasrestantes > 0:
    # Mostrar o ponto que o jogador parou
    print(" ".join([letra if letra else "_" for letra in descobertas]))

    tentativa = input("Digite uma letra: ").lower()
    acertou = False

    for i in range(len(palavraescolhida)):
        if palavraescolhida[i] == tentativa:
            descobertas[i] = tentativa
            acertou = True

    if acertou:
        pass
    else:
        print(estagioforca[7 - tentativasrestantes])
        tentativasrestantes -= 1
        if tentativasrestantes > 0:
            print("Errado! Tentativas restantes:", tentativasrestantes)
        else:
            print("Você perdeu! A palavra era:", palavraescolhida)

    palavracompleta = True
    for letra in descobertas:
        if letra == "":
            palavracompleta = False

    if palavracompleta:
        print("Parabéns! Você acertou a palavra:", palavraescolhida)
        break
