#"Len" é a função que realiza a contagem de caracteres
    #Teste: Descobrir quantos carcteres possui em senhas de uma lista--> ([])

senhas = ["abc", "segura123", "12345", "python123", "oi"]

for senha in senhas:
    if len(senha) >=6:
        print(f"A {senha} é válida, seja bem vindo!")
    else:
        print(f"A {senha} deve possuir no mínimo 6 caracteres")