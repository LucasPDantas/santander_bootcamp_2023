def sacar(valor): #abertura de bloco
    saldo = 500 #esta dentro do bloco sacar
    
    if saldo >= valor: #dentro do sacar
        print("valor sacado!") #dentro do if
        print("Retire seu dinheiro na boca do caixa!!!") #dentro do "if"
        #esses dois "print" só vai aparecer se a confiçao estiver correta
    else:
        print("O seu saldo não é suficiente, valor não sacado!") #dentro do "else", só aparece quando essa condiçao é satisfeita

    print("Obrigado por ser nosso cliente, tenha um Bom Dia.") #já esse aparece idependente da condiçao estar correta, pq esta fora do bloco do "if"


sacar(100)

