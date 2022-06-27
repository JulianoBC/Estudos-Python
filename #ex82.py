#ex82  
# Crie um programa que vai ler vários números 
# e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas
# os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das
# três listas geradas.

num = list()
pares = list()
impar = list()
while True:
    num.append(int(input('Digite um numero: ')))
    resp = str(input('quer continuar? S / N'))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impar.append(v) 
               

print(f'A lista completa é {num}')

print(f'os numeros pares são: {pares}')

print(f'os numeros impares são:{impar}')