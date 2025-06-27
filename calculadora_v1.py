print('Bem-vindo a Calculadora em Python!')

print('Qual operação deseja utilizar?\n 1.(+) Soma\n 2.(-) Subtração\n 3.(*) Multiplicação\n 4.(/) Divisão\n 5.(**) Potência\n 6.(√) Raiz Quadrada ')
operacao = input('Digite o número da operação: ')

# Verifica se é raiz quadrada (opção 6)
if operacao == '6':
    num1 = float(input('Digite o número: '))
    num2 = None  # só para manter a variável criada, mas não usada
else:
    num1 = float(input('Qual é o seu primeiro número? '))
    num2 = float(input('Qual é o seu segundo número? '))
import math

def soma(a, b):
    print(f'{a} + {b} = {a + b}')

def subtracao(a, b):
    print(f'{a} - {b} = {a - b}')

def multiplicacao(a, b):
    print(f'{a} * {b} = {a * b}')

def divisao(a, b):
    print(f'{a} / {b} = {a / b}')

def potencia(a, b):
    print(f'{a} ** {b} = {a ** b}')

def raiz(a, *b):
    print(f'√{a} = {math.sqrt(a)}')





if operacao == '1':
    soma(num1, num2)
    
elif operacao == '2':
    subtracao(num1, num2)
    
elif operacao == '3' :
    multiplicacao(num1, num2)
    
elif operacao == '4':
    divisao(num1, num2)

elif operacao == '5':
    potencia(num1, num2)

elif operacao == '6':
    raiz(num1)
else:
    print('Operação Inválida')
