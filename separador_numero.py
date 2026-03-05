numero = input('Digite um número entre 0 e 999: ') #Input pro usuário escolher seu número
numero = int(numero) #Converte a string pra número inteiro

centena = (numero//100) * 100 #Separa a centena, o comando "//" divide um número pelo outro retornando apenas a parte inteira da divisão
dezena = (((numero % 100) // 10) * 10) #Separa a dezena, o comando "%" divide um número pelo outro retornando só o resto da divisão
unidade = (numero % 100) % 10 #Separa a unidade

#Output que vai mostrar a separação do número

print('Seu número é:', numero)
print('A centena dele é:', centena)
print('A dezena dele é:', dezena)
print('A unidade dele é:', unidade)
