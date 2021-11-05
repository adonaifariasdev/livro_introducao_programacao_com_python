# Programa 3.9 - Escreva um programa que leia a quantidade de dias, horas, minutos, segundos do usuário.
# Calcule o total em segundos.
dias = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos: '))
segundos = int(input('Digite a quantidade de segundos: '))

totseg = (((dias * 24) * 60) * 60) + ((horas * 60) * 60) + (minutos * 60) + segundos
print(f'{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos, equivale a {totseg} segundos.')
