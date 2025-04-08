hora1=int(input("Digite a sua primeira hora: "))
minuto1=int(input("Digite a seu primeiro minuto: "))
hora2: int=int(input("Digite a sua segunda hora: "))
minuto2=int(input("Digite a seu segundo minuto: "))
horastotais= hora1 + hora2
minutostotais=minuto1 + minuto2
if horastotais > 12:
    horastotais = horastotais -12
if minutostotais > 12:
    minutostotais = minutostotais -60
    horastotais = horastotais + 1
print(f"Horas {horastotais}:{minutostotais} minutos")

