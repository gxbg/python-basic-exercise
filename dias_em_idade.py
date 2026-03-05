total_dias = input('Digite a idade em dias: ')
total_dias = int(total_dias)

anos = total_dias // 365
meses = (total_dias % 365) // 30
dias = (total_dias % 365) % 30

print('\n Você tem', anos, 'anos,', meses, 'meses e', dias, 'dias!')
