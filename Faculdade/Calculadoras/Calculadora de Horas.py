#Calculadora de horas

salario_mensal = input("Qual seu salário mensal? ")
horas_trabalhadas = input("Quantas horas você trabalha por mês? ")

valor_hora = float(salario_mensal) / int(horas_trabalhadas)

print(f"Você recebe R$ {valor_hora:.2f} por hora")