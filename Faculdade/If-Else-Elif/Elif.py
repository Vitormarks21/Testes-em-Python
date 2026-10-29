#Neste exemplo, o aluno está chegando atrasado na escola, e a regra da escola é:
'Se for a primeira ou segunda vez que você chega atrasado, pode entrar.'
'Mas se for a partir da terceira vez, você será suspenso.'

#Colocar o tipo de variável que queremos transformar na frente do input

atraso = int(input("Quantas faltas você possui? "))

if atraso >= 3:
    print("Você está suspenso!")
elif atraso == 2:
    print ("Mais uma falta e está suspenso!")
elif atraso == 1:
    print ("Só atrasou uma vez, pode entrar")
else:
    print("Tudo ok, vai lá")