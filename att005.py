pr = int(input('Digite um número:'))
sg = int(input('Digite o segundo número:'))
soma = pr + sg
antecessor = pr - 1
sucessor = pr + 1
ants = soma - 1
sucs = soma + 1
print(f'O seu número é {pr} e o antecessor dele é {antecessor}, o sucessor é {sucessor}', end=', ')
print(f'e a soma do item 1 e do item 2 é {soma}, sendo o antecessor dele {ants} e o sucessor {sucs}')
