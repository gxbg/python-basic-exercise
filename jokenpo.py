import random

eu = input('Escolha entre pedra papel ou tesoura: ')

esc = None

if eu == 'pedra':
  esc = 1
elif eu == 'papel':
  esc = 2
elif eu == 'tesoura':
  esc = 3
else: print('Escolha inválida')

escolhas = [0, 10 ,20]
adversario = random.choice(escolhas)

resultado = esc + adversario
if resultado == 21:
  print(f'Você escolheu {eu} e seu oponente escolheu tesoura: \n Você ganhou!')
elif resultado == 11:
  print(f'Você escolheu {eu} e seu oponente escolheu papel: \n Você perdeu :(')
elif resultado == 1:
  print(f'Você escolheu {eu} e seu oponente também! \n Empate')
elif resultado == 2:
  print(f'Você escolheu {eu} e seu oponente escolheu pedra: \n Você ganhou!')
elif resultado == 22:
  print(f'Você escolheu {eu} e seu oponente escolheu tesoura: \n Você perdeu :(')
elif resultado == 12:
  print(f'Você escolheu {eu} e seu oponente também! \n Empate')
elif resultado == 13:
  print(f'Você escolheu {eu} e seu oponente escolheu papel: \n Você ganhou!')
elif resultado == 3:
  print(f'Você escolheu {eu} e seu oponente escolheu tesoura: \n Você perdeu :(')
elif resultado == 23:
  print(f'Você escolheu {eu} e seu oponente também! \n Empate')
else: print('Escolha inválida')
