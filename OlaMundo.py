# Criando uma lista usando laço de repetição while
# Criamos uma lista vazia para armazenar os produtos digitados pelo usuário
lista_produtos = []

# Iniciamos um loop infinito — ele só vai parar quando o usuário digitar 'sair'
while True:
# Pedimos para o usuário digitar o nome da fruta
    lista_frutas = input('Nome da fruta: ')

# Usamos .lower() para converter o texto em minúsculas
    # Assim, o programa aceita "SAIR", "sair", "Sair" etc.
    if lista_frutas.lower() == 'sair':
# Se o usuário digitar 'sair', o comando break encerra o loop
        break
# Adicionamos a fruta digitada à lista de produtos
    lista_produtos.append(lista_frutas)
# Exibimos uma mensagem confirmando que o produto foi adicionado
    print(f'Produto {lista_frutas} adicionado com sucesso!')
# Quando o loop termina, mostramos a lista completa de frutas digitadas
print(f'Lista de frutas: {lista_produtos}')