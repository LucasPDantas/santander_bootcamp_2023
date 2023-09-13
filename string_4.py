# Strings de múltiplas linhas são definidas informando 3 apas simples ou duplas durante a atribuição. Elas podem ocupar várias linhas do código, e todos os espaços em brando são incluídos na string final.

nome = "Joaquim"

mensagem = f"""
Olá meu nome é {nome},
Eu estou aprendendo Python
"""
print(mensagem)


mensagem = f"""
  Olá meu nome é {nome},
Eu estou aprendendo Python
     Essa mensagem tem recuos diferentes.
"""
print(mensagem)

# útil na criação de menus
print("""
    ******************MENU*******************
    *                                       *
    *       1 - Depositar                   *
    *       2 - Sacar                       *
    *       0 - Sair                        *
    *                                       *
    *                                       *
    *  Obrigado por usar nosso sistema!!!   *
    *                                       *
    *****************************************
""")