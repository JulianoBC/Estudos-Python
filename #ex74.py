#crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla
#mostar o maior valor e o menor valor

from random import randint
num = (randint(1, 99), randint(1, 99),randint(1, 99),randint(1, 99), randint(1, 99))

print(f"eu sorteei os valores {num}")
for n in num:
    print(f'{n} ', end='')
print (f'o maior valor sorteado foi {max(num)}')
print (f'o maior valor sorteado foi {min(num)}')