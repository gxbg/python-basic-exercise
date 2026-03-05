real = input('Digite um valor em reais: ') #Input
real_float = float(real)                  #real_float deixa de ser uma string e passa a ser um número decimal

#Convertendo real para outras moedas

dolar = real_float / 5.43
euro = real_float / 6.37
libra = real_float / 7.35
iene = real_float / 0.0369
peso = real_float / 0.0038

#Output que mostra os valores convertidos, arredondados com 2 casas decimais
#O \n pula uma linha e melhora a formatação

print('\n Valor em real: R$', round(real_float,2))
print('\n Valor em dólar: $', round(dolar,2))
print('\n Valor em euro: €', round(euro,2))
print('\n Valor em libra: £',round(libra,2))
print('\n Valor em iene: ¥', round(iene,2))
print('\n Valor em pesos: $', round(peso,2))
