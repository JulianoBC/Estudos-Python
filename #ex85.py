#ex85.py
#Crie um programa onde o usuário possa digitar sete valores
# numéricos e cadastre-os em uma lista única que
# mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

num = [[], []]
valor= 0
for c in range (1, 9):
    valor = int(input('Digite o {c}o. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

print(f'-*' *30)
num[0].sort()
num[1].sort()
print(f'Digite os noves valores: {num[0]}')
print(f'os valores impares digitados foram: {num[1]}')