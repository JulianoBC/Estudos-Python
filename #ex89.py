#089.py: Crie um programa que leia nome e duas notas de vários alunos e 
#guarde tudo em uma lista composta. No final, mostre um boletim contendo a
# média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

ficha = list()
while True:
    nome = str(input('Nome :'))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2 ) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar?[s/n]'))
    if resp in "Nn":
        break
print('-*' * 30)
print(ficha)
print('-*' * 30)
for i, a  in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar as notas de qual aluno? 99 interrompe: '))
    if opc == 99:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<><>< Volte Sempre ><><><')
        

    