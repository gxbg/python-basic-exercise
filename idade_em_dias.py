anos = print('Digite sua idade em anos: ')
anos = input()
anos = int(anos)

print('Você tem', anos, 'anos e quantos meses?: ')
meses = input()
meses = int(meses)

print('Você tem', anos, 'anos,', meses, 'meses e quantos dias?: ')
dias = input()
dias = int(dias)

total_dias = (anos * 365) + (meses * 30) + dias

print('\n Parabéns, você viveu', total_dias, 'dias!')
