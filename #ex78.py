#ex78
#Crie um programa onde o usuário possa
# digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados
# , em ordem crescente.

valor = list()

while True:
    n = int(input('digite um valor: '))
    if n not in valor:
        valor.append(n)
        print('Valor adicionado com sucesso...')    
    else:
        print('valor duplicado! não vou adicionar...')
    r = str(input('quer continuar? s / n'))
    if r in 'Nn':
        break
print('-='* 30)
valor.sort()
print(f'voce digitou os valores{valor}')
