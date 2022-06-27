#ex76

list = ('lapis', 1.75,
        'borracha', 2,
        'caderno', 15,
        'estojo', 25,
        'compasso', 10,)
print('-' * 40)
print(f'{"listagem de preço":^40}')
print('-' * 40)
for pos in range(0, len(list)):
    if pos % 2 == 0:
        print(f'{list[pos]:.<30}', end='')
    else:
        print(f'R${list[pos]:>7.2f}')