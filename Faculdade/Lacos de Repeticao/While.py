#While = Repete um laço de repetição até cumprir uma condição

#Ex: Criar um programa que permite três tentativas, antes de fechar

tentativas = 0

while tentativas < 3:
    print("Tente novamente")
    tentativas = tentativas +1


#Ex 02: Só pode logar depois de digitar a senha correta

senha = ""
while senha != "123456":
   senha = input("Digite a senha correta: ")

print("Seja bem vindo!")

#Ex:03: Usuário só pode continuar depois de informar seu nome
nome = ""
while nome == "":
    nome = input("Insira seu nome para continuar: ")

print(f"Seja bem vindo {nome}!")
    