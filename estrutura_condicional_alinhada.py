conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
chqeque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com uso do cheque especial!")
    elif saque < (saldo + chqeque_especial):
        print("Saldo realizado com sucesso do Cheque Especial")
    else:
        print("Não foi possivel realizar o saque")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo não é suficiente")
else:
    print("Sistema não reconhece seu tipo de conta, procure o Gerente")   

