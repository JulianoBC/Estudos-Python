#ex84.py
#Faça um programa que leia nome e peso de várias pessoas, 
# guardando tudo em uma lista. No final, mostre:  
# A) Quantas pessoas foram cadastradas.      
# B) Uma listagem com as pessoas mais pesadas. 
# C) Uma listagem com as pessoas mais leves.

temp = []
principal = []
mai = men = 0

while True:
    
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(principal) == 0:
        mai = men = temp [1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    principal.append(temp[:])  
    temp.clear()            
    resp = str(input('Quer continuar? (S/N) '))
    if resp in 'Nn':
        break
    
    
print('-+' * 30)
#print(f'Os dados foram {principal}')
print(f'Voce cadastrou ao todo, {len(principal)}pessoas.')
print(f'o maior peso foi {mai} kg. Peso de ', end='')
for p in principal:
    if p [1] == mai:
        print(f'[{p[0]}]', end = '')
print(f'o menor peso foi de {men} kg. peso de ', end ='')
for p in principal:
    if p[1]==men:
        print(f'[{p[0]} ',end = '')