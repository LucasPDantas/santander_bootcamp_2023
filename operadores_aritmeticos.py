"""
Na matemática a definição de prioridade do cálculo na sequência é: parêntesis, expoêntes, multiplicações e divisões, por último somas e subtrações.
Quando houver operadores de mesma prioridade, a regra diz que a conta é feita da esquerda para a direita.
"""

produto_1 = 10
produto_2 = 20

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_2 / produto_1)
print(produto_2 // produto_1)
print(produto_2 * produto_1)
print(produto_2 % produto_1)
print(produto_2 ** produto_1)
print(produto_1 + produto_2 + 3.5)

x = 10 + 5 * 4
print(x)

x = (10 + 5) * 4
print(x)

y = 10 / 2 + 25 * 2 - 2 ** 2
print(y)

y = 10 / 2 + 25 * ((2 - 2) ** 2)
print(y)