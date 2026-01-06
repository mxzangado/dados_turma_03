''' 09 Elaborar um programa que efetue a apresentação do valor da conversão
em real (R$) de um valor lido em dólar (US$). O programa deverá solicitar
o valor da cotação do dólar e a quantidade de dólares disponíveis com o
usuário.'''
try:
    real = float(input('Qual valor para conversção? ').replace('.','').replace(',','.'))   # input() → sempre retorna string
    if real <0:
        raise ValueError('Não pode ser numeros negativos')             
    cota = float(input('Qual valor da cotação? ').replace('.','').replace(',','.'))
    if cota <0:
        raise ValueError('Não pode ser numeros negativos')              #Valor atual ada cotação
    dolar = real / cota                                 # Resolução 
    print('O valor de {:.2f}$ Reais \nSão: {:.2f} dolares.'.format(real,dolar)) # Mostra o resultado
except Exception as e:
    print('Apenas múmeros!',e)