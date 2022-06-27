#ex77
#Crie um programa que tenha uma tupla com várias palavras
# (não usar acentos). Depois disso, você deve mostrar, 
# para cada palavra, quais são as suas vogais.
list = ('aprender', 'almoçar', 'escola', 'casa', 'aprendizagem',
        'bagunça', 'futuro')
for p  in list:
    print(f'\n na palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'a e i o u':
            print(letra, end=' ')