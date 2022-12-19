print('Bem-vindo a Empresa de transportes e logistica RU3927883 S.A.')      #Recepção inicial com mensagem de boas vindas

def dimensoesObjeto():      #Função dimensões do objeto
    dim = 1     #Recebe o valor 1 para que qualquer número muliplicado por ele, retorne o próprio valor

    try:        #Irá tentar verificar se os valores estão de acordo com as especificações
        altura = int(input('Digite a altura do objeto (em cm):'))               #Recebe a altrua do objeto
        comprimento = int(input('Digite o comprimento do objeto (em cm):'))     #Recebe o comprimento do objeto
        largura = int(input('Digite a largura do objeto (em cm):'))             #Recebe a largura do objeto
        volume = altura * comprimento * largura         #Calcula o volume total depois de receber as medidas
        if volume < 1000:       #Verifica se o total do volume será menor que 1000
            print('O volume do objeto é (em cm³): {}'.format(volume))   #Exibe na tela o total do volume
            dim *= 10       #Se o volume for menor que 1000, recebe o valor em R$ de 10

        elif volume >= 1000 and volume < 10000:     #Verifica se o total do volume é igual ou maior que 1000 e menor que 10000
            print('O volume do objeto é (em cm³): {}'.format(volume))   #Exibe na tela o total do volume
            dim *= 20       #Se o volume for menor que 1000, recebe o valor em R$ de 20

        elif volume >= 10000 and volume < 30000:    #Verifica se o total do volume é igual ou maior que 10000 e menor que 30000
            print('O volume do objeto é (em cm³): {}'.format(volume))   #Exibe na tela o total do volume
            dim *= 30       #Se o volume for menor que 1000, recebe o valor em R$ de 30

        elif volume >= 30000 and volume < 100000:   #Verifica se o total do volume é igual ou maior que 30000 e menor que 100000
            print('O volume do objeto é (em cm³): {}'.format(volume))   #Exibe na tela o total do volume
            dim *= 50       #Se o volume for menor que 1000, recebe o valor em R$ de 50

        else:   #Se nenhuma das situações acima se concretizar, está função será exibida na tela para recomeçar o cálculo
            if volume >= 100000:    #Verifica se o total do volume é maior que 100000
                print('O volume do objeto é (em cm³): {}'.format(volume))   #Exibe na tela o total do volume
                print('Não aceitamos objetos com dimensões tão grandes!')   #Exibe na tela que a dimensão não é aceitável
                print('Entre com as dimensões novamente.')  #Avisa para entrar novamente com os valores
                return dimensoesObjeto()    #Recomeça a função novamente

    except:     #Tratamento de erro caso o usuario entre com um valor não numerico
        print('Você digitou alguma dimnesão com um valor não numérico!')    #Informa que não é aceito valores não numericos
        print('Por favor entre com as dimensões novamente.')    #Exibe o pedido para entrar com valores numericos validos
        return dimensoesObjeto()    #Recomeça a função novamente

    return dim      #Retorna o valor final sobre as dimensões


def pesoObjeto():       #Função peso do objeto
    pe = 1      #Recebe o valor 1 para que qualquer número muliplicado por ele, retorne o próprio valor
    try:        #Irá tentar verificar se os valores estão de acordo com as especificações
        peso = int(input('Entre com o peso do objeto (em kg):'))    #pede um peso válido em Kg
        if peso < 0.1:  #Verifica se o peso e menor que 0.1
            pe *= 1     #Se a verificação anteriro bater, receberá um valor de multiplicação de 1
        elif peso >= 0.1 and peso < 1:  #Verifica se o peso é igual ou maior que 0.1 e menor que 1
            pe *= 1.5   #Se a verificação anteriro bater, receberá um valor de multiplicação de 1.5
        elif peso >=1 and peso < 10:    #Verifica se o peso é igual ou maior que 1 e menor que 10
            pe *= 2     #Se a verificação anteriro bater, receberá um valor de multiplicação de 2
        elif peso >= 10 and peso < 30:      #Verifica se o peso é igual ou maior que 10 e menor que 30
            pe *= 3     #Se a verificação anteriro bater, receberá um valor de multiplicação de 3
        else:   #Se o usuario entrar com um peso inválido, essa função irá se iniciar
            if peso > 30:       #Verifica se o peso é maior que 30
                print('Não aceitamos objetos tão pesados!')     #Exibe na tela que não é aceito um peso de mais de 30kg
                print('Por favor entre com o peso novamente.')  #Exibe um pedido para inserir um peso válido
                return pesoObjeto()     #Retorna ao começo, pedindo o peso novamente

    except:     #Tratamento de erro caso o usuario entre com uma valor não numerico
        print('Você digitou o peso com um valor não numérico!')     #Exibe a mensagem informando que foi digitado um valor não numerico
        print('Por favor entre com o peso do objeto novamente.')    #Exibe o pedido para entrar novamente com o peso
        return pesoObjeto()     #Retorna ao começo, pedindo o peso novamente

    return pe   #Retorna o valor final sobre o peso


def rotaObjeto():       #Função rota do objeto
    ro = 1      #Recebe o valor 1 para que qualquer número muliplicado por ele, retorne o próprio valor

    print('Selecione a rota:')      #Faz o pedido para escolher uma rota valida
    print('RS - Rio de Janeiro até São Paulo')     #Exibe uma das opções de rota
    print('SR - São Paulo até Rio de Janeiro')  #Exibe uma das opções de rota
    print('BS - Brasília até São Paulo')    #Exibe uma das opções de rota
    print('SB - São Paulo até Brasília')    #Exibe uma das opções de rota
    print('BR - Brasília até Rio de Janeiro')   #Exibe uma das opções de rota
    print('RB - Rio de Janeiro até Brasília')   #Exibe uma das opções de rota

    rota = input('>>')      #Recebe o pedido de uma das rotas da lista acima
    if rota == 'RS' or rota == 'SR':    #Verifica se o valor inserido esta de acordo com algum da lista acima de rotas
        ro *= 1 #Recebe o valor especifico para uma das rotas especificas
    elif rota == 'BS' or rota == 'SB':  #Verifica se o valor inserido esta de acordo com algum da lista acima de rotas
        ro *= 1.2   #Recebe o valor especifico para uma das rotas especificas
    elif rota == 'BR' or rota == 'RB':  #Verifica se o valor inserido esta de acordo com algum da lista acima de rotas
        ro *= 1.5   #Recebe o valor especifico para uma das rotas especificas
    else:   #Faz um tratamento de erro caso o usuario digite uma rota que não é aceita
        print('Você digitou uma rota que não existe!')      #Exibe a mensagem que a rota não foi aceita
        print('Por favor entre com a rota do objeto novamente.')    #Exibe o pedido para digitar novamente uma rota valida
        return rotaObjeto()     #Volta ao começo da função rota

    return ro       #Retorna o valor final sobre a rota

def valor(a, b, c):     #Função que calcula o valor a ser pago após conferir as dimensões, peso e rota
    total = a * b * c   #Multiplica os valores finais recebidos
    print('O total a pagar (R$): {:.2f} (dimensões: {} * Peso: {} * Rota: {})'.format(total, a, b, c))  # Exibe o total a ser pago do transporte e os valores unitarios de dimensão, peso e rota.


valor(dimensoesObjeto(),pesoObjeto(), rotaObjeto())     #Inicia o programa o programa principal.


