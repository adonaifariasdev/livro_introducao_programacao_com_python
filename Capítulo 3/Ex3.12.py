# Programa 3.12 - Escreva um programa que  calcule o tempo de uma viagem de carro.
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = int(input('Qual a distância a percorrer(Km)? '))
velocidade = int(input('Qual a velocidade média(Km/h)? '))
tempo= distancia / velocidade
print(f'Numa viagem de {distancia}Km, numa velocidadede {velocidade}Km/h, levará um tempo de {tempo:.1f} horas.')