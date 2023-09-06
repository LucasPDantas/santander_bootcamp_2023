#sao operadores utilizados para verificar se um objeto esta presente em uma sequencia
curso = "curso de python"
frutas = ["laranja", "uva", "limao"] #lista
saques = [1500, 100] #lista

"python" in curso #"in" verifica se esta na sequencia
#True

"maça" not in frutas #"not in" verifica se nao esta na sequencia
#True

200 in saques
#False

#exemplo
frutas = ["limao", "uva"]
curso = "curso de python"

print("laranja" not in frutas)
print("limao" in frutas)
print("Pyyhon" in curso) #letras maiusculas e minusculas fazem diferenca na verificacao