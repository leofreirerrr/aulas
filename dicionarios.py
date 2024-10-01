#lista homogênea é quando só tem 1 tipo de dado, um dicionário é ula lista heterogênea
"""filme = {"nome": "Vasco da Gama", "ano": 1998, "gênero": "documentario"}

for i in filme:
    print(i, filme[i])
    
filme["ano"] = 1898

print("tabela nova")

for i in filme:
    print(i, ":", filme[i])"""
    
"""vogais = {"a": 0, "e":0, "i": 0, "o": 0, "u": 0}
frase= input("Digite a frase que voce deseja: \n")
tamanhoFrase = len(frase)
print(tamanhoFrase)
for i in range(tamanhoFrase):
    print(frase[i])
    if frase[i]=="a" or frase[i] == "A":
        vogais[frase[i]]+=1
    elif frase[i]=="e" or frase[i] == "E":
        vogais[frase[i]]+=1
    elif frase[i]=="i" or frase[i] == "I":
        vogais[frase[i]]+=1
    elif frase[i]=="o" or frase[i] == "O":
        vogais[frase[i]]+=1
    elif frase[i]=="u" or frase[i] == "U":
        vogais[frase[i]]+=1
print(vogais)"""

"""telefone = {}
opcao = 1
if opcao!=1 or opcao!= 0:
    while opcao == 1:
        novoContato = input("Digite o nome: ")
        numero = input("Dgitite  o telefone: ")
        telefone[novoContato] = numero  
        opcao = int(input("Digite 1 para continuar e 0 para sair: "))
    else:
        print("opção inválida")
print(telefone)"""

"""for i in tabela: #exemplo de como passar um for pra exibir o dicionário
    valor = tabela[i]
    print(f"{i}: {valor}")"""

"""vogais={"a":0, "e":0, "i":0, "o":0, "u":0} #outra solução pro problema das vogais
frase=input()
for letra in frase:
  if letra in vogais:
    vogais[letra]=vogais[letra]+1
print (vogais)"""

"""pessoa = {}

nomep = input("insira o seu nome: ")
idadep = int(input("insira a sua idade: "))
cidadenp = input("insira a sua cidade natal: ")
trabalhop = input("insira  o seu tabalho: ")

pessoa["nome"] = nomep
pessoa["idade"] = idadep
pessoa["cidade natal"] = cidadenp
pessoa["trabalho"] = trabalhop
print(pessoa)"""

"""computador = {"processador": 1499.00, "memoria ram": 345.00, "ssd": 482.00, "fonte": 620.00, "placa de video": 2499.00}
soma = 0
maior = 0

for i in computador:
    soma = soma+computador[i]
    if maior<computador[i]:
        maior=computador[i]
print(computador)
print(soma, maior)"""
novo = 0
esp_novo = 0
lista = []
for i in range(2):
    atleta = {}
    atleta["nome"]= (input("insira o nome do atleta: "))
    atleta["idade"]= int(input("insira a idade: "))
    atleta["esporte"] = input("insira o esporte: ")
    lista.append(atleta)

print("Relação de atletas")
for i in range(len(lista)):
    print(lista[i]["nome"], lista[i]["idade"])

esp_maisvelho = 0
idade = 0
for i in range(len(lista)):
    print(lista[i]["nome"], lista[i]["idade"])



