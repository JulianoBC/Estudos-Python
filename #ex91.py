#ex91.py : Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 99),
        'jogador2': randint(1, 99),
        'jogador3': randint(1, 99),
        'jogador4': randint(1, 99)}
rank = list()

print('Valores Sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no lançamento do dado.')
    sleep(0.1)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(rank)
for i, v in enumerate(rank):
    print(f'{i+1}º lugar : {v[0]} com {v}[1].')
