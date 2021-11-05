# Programa 4.8 - Escreva uma programa que leia dois números e que pergunte qual operação você deseja realizar.
# Você deve poder calcular soma(+), subtração(-), multiplicação(*) e divisão(/).
# Exiba o resultado da operação realizada.

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
print("""      [+] Somar
      [-] Subtrair
      [*] Multiplicar
      [/] Dividir""")
op = str(input('Operação: '))
if op == '+':
      print(f'A soma entre {a} e {b} é {a+b}.')
elif op == '-':
      print(f'A subtração entre {a} e {b} é {a - b}.')
elif op == '*':
      print(f'A multiplicação entre {a} e {b} é {a * b}.')
elif op == '/':
      print(f'A divisão entre {a} e {b} é {a / b}.')
else:
      print('Operação inválida, por favor, digite +, -, *, /')
print('FIM!')
