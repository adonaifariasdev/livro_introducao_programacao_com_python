# Programa 3.10 - Faça um programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário e a porcentagem do aumento.
# Exiba o do aumento e do novo salário.

salario_atual = float(input('Qual valor do salário atual? R$'))
aumento_porcento = int(input('Qual a porcentagem do aumento? %'))
nova_salario = salario_atual + (salario_atual * aumento_porcento / 100)
aumento = nova_salario - salario_atual
print(f'Salàrio Atual: R${salario_atual:.2f}.')
print(f'Porcentagem de aumento: {aumento_porcento}%.')
print('-' * 40)
print(f'Novo Salário: R${nova_salario:.2f}.')
print(f'Aumento de R${aumento:.2f}.')
