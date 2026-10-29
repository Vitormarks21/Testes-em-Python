#Problema - Gastos totais com o salário de todos os funcionários
#Dado uma lista de salários, calcule o total pago a todos os funcionarios

salarios = [2500, 900, 5000, 7500]
total = 0

for salario in salarios:
    #2500 -> + 900 -> + 5000 -> + 7500 = 15900
    total = total + salario

print(f"O valor total é de: R${total}")
