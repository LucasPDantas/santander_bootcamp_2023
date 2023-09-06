saldo = 2000
saque = 2500

status = "sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")

