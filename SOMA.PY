# Programa que soma números digitados até o usuário digitar 999
# Autor: Matheus Rickson Sabino da Silva

# Códigos ANSI para cores
VERDE = '\033[92m'
AMARELO = '\033[93m'
VERMELHO = '\033[91m'
CIANO = '\033[96m'
RESET = '\033[0m'

soma = cont = 0
num = 0

print(f'{CIANO}Digite números para somar. Digite 999 para parar.{RESET}')

while num != 999:
    entrada = input(f'{AMARELO}Digite um número: {RESET}')
    
    if entrada.isnumeric():  # só permite números inteiros positivos
        num = int(entrada)
        if num != 999:
            soma += num
            cont += 1
    else:
        print(f'{VERMELHO}Valor inválido! Digite apenas números inteiros positivos.{RESET}')

print(f'\n{VERDE}Você digitou {cont} números e a soma entre eles foi {soma}.{RESET}')
