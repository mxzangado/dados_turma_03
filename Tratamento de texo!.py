# Tratamento de texo!

texto = input('Digite um Texto: ')
print(' ')
print('O tipo primitivo desse valor é: =', type(texto))
print('Só tem Espaços? =', texto.isspace())
print('É um  Número? =', texto.isnumeric())
print('São Maiusculas? =', texto.isupper())
print('É Alfabetico? =', texto.isalpha())
print('É Alfanumerico? =', texto.isalnum())
print('Está em maiusula? =', texto.isupper())
print('Está em Minuscula? =', texto.islower())
print('Está Capitalizada =', texto.istitle())
print('Verifica se só tem número', texto.isdigit())