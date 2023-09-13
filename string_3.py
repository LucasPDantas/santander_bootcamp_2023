# Fatiamento de strings é uma técnica utilizada para retornar substrings (partes da string original), informando inicio (start), fim (stop) e passo (step): [start: stop[,step]]

nome = "Guilherme Arthur de Carvalho"
# os números são os índices que vai imprimir parte da string
nome[0]

nome[-2] # vai pegar a penultima letra, nesse caso "h"

nome[:9] # sem o inicío vai imprimir nesse caso 9-1, até o campo de posição 8

nome[10:] # sem o fim

nome[10:16] # inicío e fim

nome[10:16:2] # inicío, fim e intervalo, nesse caso vai de 2 em 2

nome[:] # imprimi tudo

nome[::-1] # imprimi invertido, espelhado