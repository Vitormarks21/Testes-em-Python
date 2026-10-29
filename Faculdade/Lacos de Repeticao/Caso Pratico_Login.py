#Gerenciador de Login simples

#Crie um gerenciador de login simples, com o máximo de 3 tentativas. (teremos apenas um único usuário e senha permitido)
#usuário: Vitor
#Senha: Teste3001
#Após 3 tentativas, se o usuário estiver errado exibir:
#"Aguarde 30 mins antes de tentar novamente!"
#se o usuário acertar o usuário e senha antes disso, exibir
#"Login feito com sucesso"

usuario = ""
senha = ""
tentativa = 0

while (usuario != "Vitor" or senha != "Teste3001") and tentativa < 3:
    print("\nSeja bem vindo a central de acesso")
    print("Realize o login para continuar:")
   
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
   
    tentativa += 1

    if usuario != "Vitor" or senha != "Teste3001":
        restantes = 3 - tentativa

        if restantes > 0:
            print(f"Login e/ou Senha incorretos. Você possui mais {restantes} tentativas restantes...")
        else:
            print("Tentativas esgotadas. Tente novamente em 30min.")
        

if usuario == "Vitor" and senha == "Teste3001":
    print("Login efetuado com sucesso")
    print("Redirecionando...")
