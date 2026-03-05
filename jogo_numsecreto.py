import random
num = random.randint(0, 100)  # Gera um número aleatório entre 0 e 100
chute = int(input('Advinhe o número secreto: '))

# Loop principal
while chute != num:
    if chute > num:
        chute = int(input(f'O número secreto é menor que o seu chute ({chute}). Tente novamente: '))
    elif chute < num:
        chute = int(input(f'O número secreto é maior que o seu chute ({chute}). Tente novamente: '))
    if chute == num:
        print(f'Parabéns você acertou, o número secreto é {num}')
