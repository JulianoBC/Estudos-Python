#ex81.py
#Crie um programa que vai ler vários números e 
# colocar em uma lista.                  
# Depois disso, mostre:                             
# A) Quantos números foram digitados.       
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

val = []

while True:
    val.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? S/N '))
    if resp in 'Nn':
        break
print(f'Voce digitou {len(val)} elementos')
val.sort(reverse=True)
print(f'os valores em forma decrescente {val}')
if 5 in val:
    print('o valor 5 faz parte da lista')
else: print('o valor 5 não foi encontrado na lista!')
