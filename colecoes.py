#Listas

# precos = [20,50,100]
# print(precos[1]) # acessando por Índice

# nomes = ["Brazil", "EUA", "México"]
# print(nomes[2]) # acessando por Índice

# Encontrar o índice de forma automática
# print(nomes.index('EUA'))

# Manipular - Adicionar novos itens
# salarios = [2500, 5000, 7000]
# salario_usuario = float(input('Qual é o seu salário: '))
# salarios.append(salario_usuario)
# print(salarios)

# Problema - Gastos totais com pagamento de salários.
# Dado uma lista de salários, calcule o total pago a todos os funcionários
'''
# Método 5Q's para montar um algorítimo:

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais
informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- lista de salários

2. O que devo fazer com estes dados?
- somar um com o outro até finalizar a lista de salários

3. Quais são as restrições deste problema?
- precisamos de uma lista com no mínimo 2 salários

4. Qual é o resultado esperado?
- exibir a soma de todos os salários

5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
(pseudocódigo)
- receber uma lista de salários
- somar cada valor da lista até obter o total
- exibir o total gasto com pagamentos de salários

'''
salarios = [100, 200, 100, 100]
total = 0
for salario in salarios:
    total = total + salario 
print(total)