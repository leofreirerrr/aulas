"""import random
matriz = []

for i in range(3): #versão resumida de como armazenar os valores na matriz
    matriz.append([])
    for j in range(3):
        matriz[i].append(int(input(random.randint())))

for i in range(3): #mostrando a matriz po linha
    print(matriz[i])
        
#achar o menor elemento por linha
for i in range(3):
    menor = matriz [i] [0]
    for j in range(3):
        if matriz[i][j]<menor:
            menor = matriz [i][j]
    print("Menor: ", menor)
    
#achar o menor elemento da matriz inteira
for i in range(3): 
    for j in range(3):
        if matriz[i] [j] < menor:
            menor = matriz[i][j]
            linhaMenor = [i]
print(f"o menor é {menor} e está na linha {linhaMenor}")

#matriz diagonal
cont = 0
for i in range(3):
    for i in range(3):
        if i!=j and matriz[i] [j] == 0:
            cont = cont+1
            
if cont == 0:
    print(1)
else:
    print(0)"""

gabarito = input("insira o gabarito: ").split()

alunos = []
for i in range(3):
    alunos.append(input("insira as respostas dos alunos: ").split())

contador = 0
for i in range(3):
    nota = 0
    for j in range(len(gabarito)):
        if alunos[i][j] == gabarito[j]:
            nota = nota+12.5
    print(nota)




