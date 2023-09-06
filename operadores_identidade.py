#operadores sao utilizados para comparar se os dois objetos testados ocupam a mesma posicao na memoria.

curso = "curso de python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso
#True

curso is not nome_curso
#False

saldo is limite
#True

#exemplo
saldo = 1000
limite = 500 #nao ocupa a mesma regiao da memoria

print(saldo is limite)
print(saldo is not limite)

saldo = 1000
limite = 1000 #ocupa a mesma regiao da memoria

print(saldo is limite) #com "is" eu verifico se esta na mesma memoria
print(saldo is not limite) #com "is not" eu verifico se nao esta na mesma regiao da memoria