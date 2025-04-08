time1=input("Digite o nome do seu time: ")
time2=input("Digite o nome do seu time: ")
goltime1=int(input(f"Digite a quantidade de gol's do {time1} na partida: "))
goltime2=int(input(f"Digite a quantidade de gol's do {time2} na partida: "))
if time1 > time2:
    print(f"{time1} vence {time2} por {goltime1}x{goltime2}")
elif time1 == time2:
    print(f"partida entre {time1} e {time2} empata  por {goltime1}x{goltime2}")
else:
    print(f"{time1} perde para o {time2} com o placar de {goltime1}x{goltime2} ")