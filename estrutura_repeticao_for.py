#esse código esta separando as vogais de um texto

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print() #adiciona uma quebra de linha

#exemplo utilizando a funçao built-in range
for numero in range(0, 51, 5): #tabuada do cinco
    print(numero, end="") #"end=" vai fazer os números aparecerem lado a lado

