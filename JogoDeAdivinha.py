import random
print('''Sou seu computador...
Pensei em numero entre 0 e 10.
você consegue adivinhar?!''')
computador = random.randint(0,10)
acertou = False
palpite = 0
while not acertou:
    palyer = int(input('Qualo seu palpite?'))
    palpite += 1
    if palyer == computador:
        acertou = True
        print('Parabéns, você acertou com {} tentaivas!'.format(palpite))
    else:
        if palyer < computador:
            print('Mais...')
        elif palyer > computador:
            print('Menos...')

