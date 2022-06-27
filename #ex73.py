num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito',
        'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte' )

#ordenar essas palavras em ordens sequencias, as primeiras 5 palavras
#os ultimos 4 colocados
#os numeros em ordem alfabética
#qual posição está o numero dez
print('-=' *15)
print (f'lista de numeros: {num}')
print('-=' *15)
print(f'os cinco primeiros numeros {num[0:5]}')
print('-=' *15)
print(f'os ultimos 4 numeros{num[-4:]}')
print('-=' *15)
print(f'os numeros em ordem alfabética {sorted(num)}')
print('-=' *15)
print(f'A posição do numero dez é {num.index("dez")+1} na lista')