nome = "Joana"
idade = 35
profissao  = "Dentista"
linguagem = "Portugues"
saldo = 100.5894

dados = {"nome": "Joana", "idade": 35} # dicionário

print("nome: %s idade: %d" % (nome, idade))

print("nome: {} idade: {}".format(nome, idade))

print("nome: {1} idade: {0}".format(idade, nome))

print("nome: {nome} idade: {idade}".format(nome=nome, idade=idade))

print("nome: {nome} idade: {idade}".format(**dados)) # dicionário sendo usado

print(f"nome: {nome} idade: {idade}")
print(f"nome: {nome} idade: {idade} saldo: {saldo:.2f}")
print(f"nome: {nome} idade: {idade} saldo: {saldo:10.2f}")