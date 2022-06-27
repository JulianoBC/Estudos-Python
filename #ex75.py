#ex75
#qts vezes apareceu o 9
#em que posição apareceu o valor 3
#quais foram os numeros pares
num = (int(input('Digite um numero: ')),
        int(input('Digite um numero: ')),
        int(input('Digite um numero: ')),
        int(input('Digite um numero: ')))
print(f'voce digitou os valores {num}')
print(f'o valor 9 apareceu {num.count(9)}vezes')
if 3 in num:
    print(f'o valor 3 apareceu na {num.index(3)+1}')
else:
    print(f' o valor 3 não foi digitado em nenhuma posição')
print('os valores digitados pares foram ', end='') 
for n in num:
    if n % 2 ==0:
        print (n, end='')