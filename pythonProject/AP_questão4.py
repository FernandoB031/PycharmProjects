# Função de cadastro das peças
def cadastrarPeca(codigo):

    print('Você escolheu cadastra peças.')      # Confirma sua escolha
    print('O código da peça 00{}'.format(codigo))   #Atribui o código a cada cadastro apos o calculo

    nome = input('Digite o nome da peça:')  # Entrada do nome da peça
    fabricante = input('Digite o Fabricante da peça:')  # Entrada do nome do Fabricante
    valor = float(input('Digite o valor (em R$) da peça:'))     # Entrada do valor em reais da peça

    dicCadastro = {'Código'     : codigo,   #Cria um dicionário para armazenar os cadastros
                   'Nome'       : nome,
                   'Fabricante' : fabricante,
                   'Valor'      : valor}

    listaCadastro.append(dicCadastro.copy()) # Cria uma cópia do dicionario na lista

# Função de consulta das peças
def consultarPeca():

    print('Você escolheu consultar peças.')     # Confirma sua escolha

    consulta = int(input('Escolha a opção desejada:\n'
                         '1 - Consultar todas as peças\n'   # Faz uma consulta de todas peças cadastradas
                         '2 - Consultar peças por código\n' # Faz uma consulta de todas peças cadastradas por código
                         '3 - Consultar peças por Fabricante\n' # Faz uma consulta de todas peças cadastradas por Fabricante
                         '4 - Retornar\n'   # Retorna ao menu inicial
                         '>>'))

    if consulta == 1:   # Se esta for a escolha, exibe todas as peças cadastradas de uma forma geral
        print('Você escolheu consultar todas as peças.')    # Confirma sua escolha
        print('-' * 30) # Detalhe de acabamento
        for cadastro in listaCadastro:
            for key, value in cadastro.items():
                print('{} : {}'.format(key, value))
        print('-' * 30) # Detalhe de acabamento
        consultarPeca()     #Retorna ao menu de consulta

    elif consulta == 2: # Se esta for a escolha, exibe todas as peças cadastradas através do código
        print('Você escolheu consultar peças por código.')  # Confirma sua escolha

        conscod = int(input('Digite o código da peça:'))
        print('-' * 30) # Detalhe de acabamento
        for cadastro in listaCadastro:
            if (cadastro['Código'] == conscod):
                for key, value in cadastro.items():
                    print('{} : {}'.format(key, value))
        print('-' * 30) # Detalhe de acabamento
        consultarPeca()     #Retorna ao menu de consulta

    elif consulta == 3: # Se esta for a escolha, exibe todas as peças cadastradas através do Fabricante
        print('Você escolheu consultar peças por Fabricante.')  # Confirma sua escolha

        consfabri = input('Digite o Fabricante da peça:')
        print('-' * 30) # Detalhe de acabamento
        for cadastro in listaCadastro:
            if (cadastro['Fabricante'] == consfabri):
                for key, value in cadastro.items():
                    print('{} : {}'.format(key, value))
        print('-' * 30) # Detalhe de acabamento
        consultarPeca() # Retorna ao menu de consulta

    elif consulta == 4:  # Se esta for a escolha, retorna ao menu anterior
        return

# Função para remover um dos cadastro de peças
def removerPeca():

    print('Você escolheu remover peças.')   # Confirma sua escolha

    remove = int(input('Digite o código das peças que deseja remover:')) # Faz o pedido para inserir o código da peça a ser deletada
    for cadastro in listaCadastro:
        if (cadastro['Código'] == remove):
            listaCadastro.remove(cadastro)


# Começo do programa
print('-' * 60) # Detalhe de acabamento
print('Bem-Vindo ao controle de estoque da Bicicletaria RU3927883') #Mensagem de Boas-Vindas
print('-' * 60) # Detalhe de acabamento

codigo = 0  #Variavel que atribui um codigo a peça que esta sendo cadastrada
listaCadastro = []  # Lista  completa a ser preechida por cadastros das peças

while True: # Inicia um laço de repetição obrigando alguma das opções abaixo a se realizarem

    inicio = int(input('Escolha a opção desejada:\n'    # Exibe o menu de opções inicias
                       '1 - Cadastrar peças\n'  # Começar cadastro
                       '2 - Consultar peças\n'  # Consultar um cadastro já existente
                       '3 - Remover peças\n'    # Remove um cadastro já existente
                       '4 - Sair\n' # finaliza o programa
                       '>>'))

    if inicio == 1:     # Se esta opção for escolhida, se inicia a função cadastro

        codigo += 1     # Atribui  um calculo fazendo que o primeiro cadastro se inicie em 1
        cadastrarPeca(codigo)   # invoca a função de cadastro

    elif inicio == 2:   # Se esta opção for escolhida, se inicia a função de consulta

        consultarPeca() # invoca a função de consulta

    elif inicio == 3:   ## Se esta opção for escolhida, se inicia a função de remover cadastro

        removerPeca()   # invoca a função de remover

    elif inicio == 4:   # Se esta opção for ecolhida, finaliza o programa

        break

    else:   # Se nenhuma das opções do menu acima forem escolhidas, ficara sempre perguntando uma opção valida
        print('Por favor digite uma opção válida do menu!') #exibe a mensagem de aviso
        continue

