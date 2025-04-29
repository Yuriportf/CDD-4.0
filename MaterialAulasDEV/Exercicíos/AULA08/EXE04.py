A = [5,6,7,8,9]
numero = int(input("Digite o seu valor: "))
novo = [""]*5
for i in range (len(A)):
    novo[i]=numero*A[i]
print(novo)