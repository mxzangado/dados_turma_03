
nome = input('Digite seu nome: ')
print(f'Olá, mundo {nome}!')

idade = int(input('Digite a sua idade: '))
if (idade) >= 18:
    print('Voce eh maior de idade.')
else:
    print('Voce eh menor de idade')
    
for i in range(1, idade+1):
    print(i)