# Programa 3.11 - Façaum programa que solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar.

preço = float(input('Qual valor da mercadoria? R$'))
desconto = int(input('Qual valor do desconto? '))
preço_novo = preço - (preço * desconto / 100)
print(f'PREÇO NORMAL R${preço:.2f}.')
print(f'DESCONTO DE {desconto}% É R${preço - preço_novo:.2f}.')
print(f'TOTAL A PAGAR R${preço_novo:.2f}.')