
# Fazendo uma soma entre dois números
try:
    n1 = int(input('Digite um Número: '))
    n2 = int(input('Digite Outro Número: '))

    soma = n1 + n2
    resultado = soma
    print(f'O resultadode {n1} + {n2} é = {resultado}')
except ValueError:
    print("Por favor, digite apenas números inteiros.")

