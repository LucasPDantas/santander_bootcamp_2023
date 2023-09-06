#while True:
#    numero = int(input("Informe um número: "))

#    if numero == 10:
#        break #condiçao de parada

#    print(numero)

"""
for numero in range(100):

    if numero == 10:
        break

    print(numero)
"""

for numero in range(25):

    if numero == 12: #vai pular o "12" e continuar
        continue #faz com que o programa pule a condicao e contue o código

    print(numero, end=" ")

print()

for numero in range(25):

    if numero % 2 == 0: #vai pular todos os numeros pares
        continue 

    print(numero, end=" ")


#da para usar o "break" e o "continue" juntos
while True:
    numero = int(input("Informe um número: "))

    if numero == 10: # se aparecer um numero "10" ele vai parar o codigo
        break

    if numero % 2 == 0: #vai printar só os numeros ímpares
        continue

    print(numero)