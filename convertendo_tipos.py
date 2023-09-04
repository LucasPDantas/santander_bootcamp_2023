preco = 10
print(preco)
#em cima tenho um valor int e em baixo estou convertendo ele para float#
preco = float(preco)
print(preco)

preco = 10.30
print(preco)
#aqui está acontecendo o contrário, estou mudando o de cima que é float, para o de baixo que é int#
preco = int(preco)
print(preco)

print(preco / 2)
#na divisão para converter o float acima para o int embaixo, usamos (//)#
print(preco // 2)

preco = 10.50
idade = 28

print(str(preco))
#convertendo número para string(str)#
print(str(idade))

texto = f"idade {idade} preco {preco}"
print(texto)

preco = "10.50"
idade = "28"

print(float(preco))
#convertendo str para número, float e int#
print(int(idade))

'''
preco = "python"
print(float(preco)) #nesse caso vai haver um erro, pois não é possível converter caracteres para número#
'''

#exemplos#
print(int(1.9899974))
print(int("10"))
print(float("10.10"))
print(float(100))

print(str(10.30))
print(type(str(10.30)))
