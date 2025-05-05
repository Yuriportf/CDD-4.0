def recebernome(nome):
    print(nome)

def imprimiernumero(t):
    for i in range(1,t+1,1):
        for x in range(0,i):
            print(i, end=" ")
        print()

"""def contarvogal(texto):
 for i in range(len(texto)):
     if i in "aeiou":
        cont+=1
    print(cont)"""

def estoque(produto,quantidade,valor):
    calculo = quantidade * valor
    return  produto,calculo

def postivonegat(numero):
    if numero > 0:
        return " P "
    elif numero < 0:
        return " N "
    elif numero == 0:
        return " z "
    else:
        pass

def cal (*num):
    cont =0
    for i in range(len(num)):
       cont+=num[i]
    print(cont)

def contatexto (texto):
    if texto == " ":
       texto= texto - " "
       cont=0
       for i in range(len(texto)):
          print (texto[i])
          cont+=1
       for i in range(len(texto,)-1,-1,-1):
         return (texto[i])

def letras(texto):
 cont = 0
 if letras == " ":
     for i in range(len(texto)-1,-1,-1):
         print(texto[i])
         if texto[i] not in " ":
             cont+=1
         print(f"{cont}")

def remover ():
    L1 =[10,12,12,31,4,4,5,31,6,7,8]
    NEW = [""]
    for i in range(len(L1)):
        if L1[i] == [i]:
            print(L1)

def lista(L):
    listan=[]
    for i in L:
      if i not in lista:
         lista.append(i)
    print(L)
    print(listan)




