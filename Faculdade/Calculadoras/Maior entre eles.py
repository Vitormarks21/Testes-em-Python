#Problema:
# Crie um programa que recebe dois valores e exibe qual é o maior entre eles.

primeiro_numero = int(input("Digite o primeiro valor: "))
segundo_numero = int(input("Digite o segundo valor: "))

if primeiro_numero > segundo_numero:
    print(f"O {primeiro_numero} é maior que {segundo_numero}.")
elif primeiro_numero == segundo_numero:
    print(f"Os números {primeiro_numero} e {segundo_numero} são iguais.")
    
else:
    print(f"O {segundo_numero} é maior que {primeiro_numero}.")