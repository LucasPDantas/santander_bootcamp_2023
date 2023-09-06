#tabela verdade
print(True and True) #True
print(True and False) #False
print(False and False) #False
print(True or True) #True
print(True or False) #True
print(False or False) #False
"""
Em Python, os operadores lógicos são usados para realizar operações lógicas em valores booleanos (True ou False). Existem três operadores lógicos principais em Python: "and", "or" e "not". Aqui está uma breve explicação de cada um deles:

Operador "and":
Sintaxe: condição1 and condição2
Retorna True se ambas as condições condição1 e condição2 forem True; caso contrário, retorna False.
"""
#exemplo#
x = True
y = False
resultado = x and y
print(resultado)  # O resultado será False

saldo = 1000
saque = 200
limite = 100
saldo >= saque and saque <= limite
#False

"""
Operador "or":
Sintaxe: condição1 or condição2
Retorna True se pelo menos uma das condições condição1 ou condição2 for True; retorna False apenas se ambas forem False.
"""
#exemplo#
x = True
y = False
resultado = x or y  # O resultado será True
print(resultado)

saldo = 1000
saque = 200
limite = 100
saldo >= saque or saque <= limite
#True

"""
Operador "not":
Sintaxe: not condição
Retorna o oposto do valor da condição. Se a condição for True, "not" a tornará False, e se a condição for False, "not" a tornará True.
"""
#exemplo#
x = True
resultado = not x  # O resultado será False
print(resultado)

contatos_emergencia = [] #lista vazia, valor booleano é False

not 1000 > 1500
#True

not contatos_emergencia
#True

not "saque 1500;"
#False

not "" #str vazia, é considerada False
#True

"""
expressões lógicas mais complexas.
"""
#exemplo#
a = True
b = False
c = True

resultado = a and (b or c)
print(resultado)  # O resultado será True, Neste exemplo, a expressão avalia primeiro 'b or c', que resulta em True, e depois avalia 'a and True', resultando em True no final.

#parênteses
saldo = 1000
saque = 250
limite = 200
conta_especial = True

expressao1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque #True
print(expressao1)

expressao2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) #dessa forma fica mais legivel o código
print(expressao2) 
#True

#deixar a expressao acima mais legivel, dividindo em bloco para não haver uma exprassao muito grande.
conta_normal_com_saldo_suficiente = saldo >= saque and limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

expressao3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(expressao3)