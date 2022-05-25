# Primeiro teste feito utilizando o int
print('Digite dois números e eles serão somados.')
primeiro = int(input('Digite o primeiro numero'))
segundo = int(input('Digite o segundo numero'))
soma = primeiro + segundo
print('A soma desses dois números é {}'.format(soma))

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
soma = n1 + n2
# print('A soma entre',n1,'e',n2,'vale',soma) << teste do print feito com uso de virgula.
print(f'A soma entre {n1} e {n2} vale {soma}!') # << teste do print usando chaves.