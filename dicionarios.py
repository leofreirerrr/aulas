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

telefone = {}
opcao = int(input("Digite 1 para continuar e 0 para sair: "))
if opcao!=1 or opcao!= 0:
    while opcao == 1:
        novoContato = input("Digite o nome: ")
        numero = input("Dgitite  o telefone: ")
        telefone[novoContato] = numero  
        opcao = int(input("Digite 1 para continuar e 0 para sair: "))
    else:
        print("opção inválida")
print(telefone)