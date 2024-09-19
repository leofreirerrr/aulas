matriz = []

"""for i in range(4): #preenchendo a tabela
    linha = []
    for j in range(4):
        elemento = int(input("digite um valor: "))
        linha.append(elemento)
    matriz.append(linha)


for i in range(4): #mostrando a matriz em forma de tabela
    for j in range(4):
        print(matriz[i] [j], end=" ")
    print()    """     
            
"""for i in range(3): #outro jeito de preencher  tabela
    matriz.append([])
    for j in range(3):
        elemento = int(input("digite um valor: "))
        matriz[i].append(elemento)
print(matriz)"""

"""print("diagonal principal")
for i in range(3):
    print(matriz[i][i])
    
print("Diagonal secundária")
for i in range(3):
    for j in range(3):
        if i+j == len(matriz)-1:
            print(matriz[i][j])"""
            
"""print("zigzag")
for i in range(4):
    if i%2!=0:
        for j in range(4):
            print(matriz[i][j], end=" ")
    else:
        for j in range(len(matriz)-1, -1, -1):
            print(matriz[i][j])
    print()"""

#achar a linha do menor elemento

linhaMenor = 0

n = int(input("digite o valor da matriz quadrada: "))

for i in range(n): #outro jeito de preencher  tabela
    matriz.append([])
    for j in range(n):
        elemento = int(input("digite um valor: "))
        matriz[i].append(elemento)
    
menor = matriz[0][0]

for i in range(n):
    for j in range(n):
        if matriz[i] [j] < menor:
            menor = matriz[i][j]
            linhaMenor = [i]
print(f"o menor é {menor} e está na linha {linhaMenor}")
        