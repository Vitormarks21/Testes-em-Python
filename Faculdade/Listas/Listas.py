#Listas
preço = [20, 50, 100]
#       [ 0,  1,  2]
#Os itens de uma lista podem ser encontrados pela ordem em que estão (considerando o primeiro item como 0)

print(preço[2])

#Esta numeração dos itens é chamada de "ÍNDICE"
#Para encontrar o índice de um item de uma lista (você não precisa ficar contando item por item no código) se usa a função "index".

print(preço.index(100)) 

#Se a lista tivesse nomes, seria necessário colocas aspas na busca, mas como o exemplo contém numeros, não é necessário.
#Uma lista pode várias variáveis misturadas, (valores númericos, booleanos, textos)

#--------------------------Como manipular uma lista

#Manipular = adicionar novos itens
salarios = [2500, 5000, 7000]
salario_usuario = float(input("Qual o seu salário? "))
salarios.append(salario_usuario)

print(salarios)

#O comando "print(salarios)" imprime toda a lista para o usuario ver.