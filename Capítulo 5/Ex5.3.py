# Programa 5.3 - Faça um programa para escrever a contagem regressiva do lançamento de um foguete.
# O programa deve imprimir 10, 9, 8..., 1, 0 e FOGO! na tela.
from time import sleep
c = 10
while c >= 0:
    print(c, end=' -> ')
    sleep(1)
    c -= 1
print('FOGO!!!!!')