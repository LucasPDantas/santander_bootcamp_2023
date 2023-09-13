nome = "noTeBooK"

print(nome.upper()) # deixa tudo em maiusculo
print(nome.lower()) # em minusculo
print(nome.title()) # primeira letra em maiusculo

texto = " olá mundo!  "

print(texto)
print(texto.strip()) # tira os espaços
print(texto.lstrip()) # remove o espaço da esquerda
print(texto.rstrip()) # remove o espaço da direita

print(texto + ".")
print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")

# centralizaçao
menu = "Python"

print("###" + menu + "###")
print(menu.center(14))
print(menu.center(14, "#"))

print("P-y-t-h-o-n")
print("-".join(menu)) # separaçao