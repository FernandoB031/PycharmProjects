print('Bem-vindo a Lanchonete RU3927883!') #boas-vindas ao Programa

d1 = '*' * 18   #detalhe na exibição do cardápio
d2 = '|'        #detalhe na exibição do cardápio
d3 = '-' * 60       #detalhe na exibição do agradecimento ao finalizar o pedido
print(' ' * 40)     #detalhe na exibição do cardápio
print(d1 + ' Cardápio ' + d1)       #exibição do texto cardápio
print(' ')                     #espacamento do texto para o menu
print(d2 + ' Codigo ' + d2 + ' ' * 8 + 'Descrição' + ' ' * 10 + d2 + ' Valor ' + d2)        #começo da exibição do menu
print(d2 + '   100  ' + d2 + ' ' * 8 + 'Cachorro-quente' + ' ' * 4 + d2 + ' 9,00  ' + d2)   #exibe a opção um com seu respectivo valor
print(d2 + '   101  ' + d2 + ' ' * 4 + 'Cachorro-quente duplo' + ' ' * 2 + d2 + ' 11,00 ' + d2)     #exibe a opção dois com seu respectivo valor
print(d2 + '   102  ' + d2 + ' ' * 12 + 'X-egg' + ' ' * 10 + d2 + ' 12,00 ' + d2)       #exibe a opção três com seu respectivo valor
print(d2 + '   103  ' + d2 + ' ' * 10 + 'X-salada' + ' ' * 9 + d2 + ' 12,00 ' + d2)     #exibe a opção quatro com seu respectivo valor
print(d2 + '   104  ' + d2 + ' ' * 10 + 'X-bacon' + ' ' * 10 + d2 + ' 14,00 ' + d2)     #exibe a opção cinco com seu respectivo valor
print(d2 + '   105  ' + d2 + ' ' * 10 + 'X-tudo' + ' ' * 11 + d2 + ' 17,00 ' + d2)      #exibe a opção seis com seu respectivo valor
print(d2 + '   200  ' + d2 + ' ' * 3 + 'Refrigerante em lata' + ' ' * 4 + d2 + ' 5,00  ' + d2)      #exibe a opção sete com seu respectivo valor
print(d2 + '   201  ' + d2 + ' ' * 8 + 'Chá gelado' + ' ' * 9 + d2 + ' 4,00  ' + d2)        #exibe a opção oito com seu respectivo valor
print(' ' * 40)

preco1 = 4      #variável preço do Chá gelado
preco2 = 5      #variável preço do Refrigerante em lata
preco3 = 9      #variável preço do Cachorro-quente
preco4 = 11     #variável preço do Cachorro-quente duplo
preco5 = 12     #variável preço do X-egg / X-salada
preco6 = 14     #variável preço do X-bacon
preco7 = 17     #variável preço do X-tudo
soma = 0        #Variavel soma que irá exibir o preço total

while True:     #inicio do laço
    ini = int(input('Entre com o código do produto:'))      #entrada do codigo do produto escolhido

    if (ini == 100):    #verifica se o codigo é referente ao Cachorro-quente
        print('Você pediu um Cachorro-quente no valor de 9,00')     #valor referente ao Cachorro-quente
        soma += preco3      #realiza a soma ou recebimento do valor adequado
        print('Gostaria de pedir mais alguma coisa?')   #pergunta se tem interesse em mais um pedido
        print('1 - Sim')    #opção aceitar para prosseguir
        print('0 - Não')    #opção negar para finalizar
        pergunta = int(input('>>'))     #recebe a opção escolhida
        if (pergunta != 1):     #verifica se a opção é diferente de verdadeiro (aceitar)
            print('O valor total da conta é:R${:.2f}'.format(soma))     #exibe o(os) valor(es) total(is) a pagar
            print(d3)       #exibe o detalhe sobre os agradecimentos finais
            print('A Lanchonete RU3927883 agradece a preferência, volte sempre!')   #agradecimento final pela escolha da lanchonete
            print(d3)       #exibe o detalhe sobre os agradecimentos finais
            break       #pausa e finaliza a operação

    elif (ini == 101):      #verifica se o codigo é referente ao Cachorro-quente duplo
        print('Você pediu um Cachorro-qunete duplo no valor de 11,00')      #valor referente ao Cachorro-quente duplo
        soma += preco4      #realiza a soma ou recebimento do valor adequado
        print('Gostaria de pedir mais alguma coisa?')       #pergunta se tem interesse em mais um pedido
        print('1 - Sim')        #opção aceitar para prosseguir
        print('0 - Não')        #opção negar para finalizar
        pergunta = int(input('>>'))     #recebe a opção escolhida
        if (pergunta != 1):     #verifica se a opção é diferente de verdadeiro (aceitar)
            print('O valor total da conta é:R${:.2f}'.format(soma))     #exibe o(os) valor(es) total(is) a pagar
            print(d3)       #exibe o detalhe sobre os agradecimentos finais
            print('A Lanchonete RU3927883 agradece a preferência, volte sempre!')   #agradecimento final pela escolha da lanchonete
            print(d3)       #exibe o detalhe sobre os agradecimentos finais
            break       #pausa e finaliza a operação

    elif (ini == 102):      #verifica se o codigo é referente ao X-egg
        print('Você pediu um X-egg no valor de 12,00')      #valor referente ao X-egg
        soma += preco5      #realiza a soma ou recebimento do valor adequado
        print('Gostaria de pedir mais alguma coisa?')       #pergunta se tem interesse em mais um pedido
        print('1 - Sim')        #opção aceitar para prosseguir
        print('0 - Não')        #opção negar para finalizar
        pergunta = int(input('>>'))     #recebe a opção escolhida
        if (pergunta != 1):     #verifica se a opção é diferente de verdadeiro (aceitar)
            print('O valor total da conta é:R${:.2f}'.format(soma))     #exibe o(os) valor(es) total(is) a pagar
            print(d3)       #exibe o detalhe sobre os agradecimentos finais
            print('A Lanchonete RU3927883 agradece a preferência, volte sempre!')   #agradecimento final pela escolha da lanchonete
            print(d3)       #exibe o detalhe sobre os agradecimentos finais
            break       #pausa e finaliza a operação

    elif (ini == 103):      #verifica se o codigo é referente ao X-salada
        print('Você pediu um X-salada no valor de 12,00')       #valor referente ao X-salada
        soma += preco5      #realiza a soma ou recebimento do valor adequado
        print('Gostaria de pedir mais alguma coisa?')       #pergunta se tem interesse em mais um pedido
        print('1 - Sim')        #opção aceitar para prosseguir
        print('0 - Não')        #opção negar para finalizar
        pergunta = int(input('>>'))     #recebe a opção escolhida
        if (pergunta != 1):     #verifica se a opção é diferente de verdadeiro (aceitar)
            print('O valor total da conta é:R${:.2f}'.format(soma))     #exibe o(os) valor(es) total(is) a pagar
            print(d3)       #exibe o detalhe sobre os agradecimentos finais
            print('A Lanchonete RU3927883 agradece a preferência, volte sempre!')   #agradecimento final pela escolha da lanchonete
            print(d3)       #exibe o detalhe sobre os agradecimentos finais
            break   #pausa e finaliza a operação

    elif (ini == 104):      #verifica se o codigo é referente ao X-bacon
        print('Você pediu um X-bacon no valor de 14,00')        #valor referente ao X-bacon
        soma += preco6      #realiza a soma ou recebimento do valor adequado
        print('Gostaria de pedir mais alguma coisa?')       #pergunta se tem interesse em mais um pedido
        print('1 - Sim')        #opção aceitar para prosseguir
        print('0 - Não')        #opção negar para finalizar
        pergunta = int(input('>>'))     #recebe a opção escolhida
        if (pergunta != 1):     #verifica se a opção é diferente de verdadeiro (aceitar)
            print('O valor total da conta é:R${:.2f}'.format(soma))     #exibe o(os) valor(es) total(is) a pagar
            print(d3)       #exibe o detalhe sobre os agradecimentos finais
            print('A Lanchonete RU3927883 agradece a preferência, volte sempre!')   #agradecimento final pela escolha da lanchonete
            print(d3)       #exibe o detalhe sobre os agradecimentos finais
            break   #pausa e finaliza a operação

    elif (ini == 105):      #verifica se o codigo é referente ao X-tudo
        print('Você pediu um X-tudo no valor de 17,00')     #valor referente ao X-tudo
        soma += preco7      #realiza a soma ou recebimento do valor adequado
        print('Gostaria de pedir mais alguma coisa?')       #pergunta se tem interesse em mais um pedido
        print('1 - Sim')        #opção aceitar para prosseguir
        print('0 - Não')        #opção negar para finalizar
        pergunta = int(input('>>'))     #recebe a opção escolhida
        if (pergunta != 1):     #verifica se a opção é diferente de verdadeiro (aceitar)
            print('O valor total da conta é:R${:.2f}'.format(soma))     #exibe o(os) valor(es) total(is) a pagar
            print(d3)       #exibe o detalhe sobre os agradecimentos finais
            print('A Lanchonete RU3927883 agradece a preferência, volte sempre!')   #agradecimento final pela escolha da lanchonete
            print(d3)       #exibe o detalhe sobre os agradecimentos finais
            break   #pausa e finaliza a operação

    elif (ini == 200):      #verifica se o codigo é referente ao Refrigerante em lata
        print('Você pediu um Refrigerante em lata no valor de 5,00')        #valor referente ao Refrigerante em lata
        soma += preco2      #realiza a soma ou recebimento do valor adequado
        print('Gostaria de pedir mais alguma coisa?')       #pergunta se tem interesse em mais um pedido
        print('1 - Sim')        #opção aceitar para prosseguir
        print('0 - Não')        #opção negar para finalizar
        pergunta = int(input('>>'))     #recebe a opção escolhida
        if (pergunta != 1):     #verifica se a opção é diferente de verdadeiro (aceitar)
            print('O valor total da conta é:R${:.2f}'.format(soma))     #exibe o(os) valor(es) total(is) a pagar
            print(d3)       #exibe o detalhe sobre os agradecimentos finais
            print('A Lanchonete RU3927883 agradece a preferência, volte sempre!')   #agradecimento final pela escolha da lanchonete
            print(d3)       #exibe o detalhe sobre os agradecimentos finais
            break   #pausa e finaliza a operação

    elif (ini == 201):      #verifica se o codigo é referente ao Chá gelado
        print('Você pediu um Chá gelado no valor de 4,00')      #valor referente ao Chá gelado
        soma += preco1      #realiza a soma ou recebimento do valor adequado
        print('Gostaria de pedir mais alguma coisa?')       #pergunta se tem interesse em mais um pedido
        print('1 - Sim')        #opção aceitar para prosseguir
        print('0 - Não')        #opção negar para finalizar
        pergunta = int(input('>>'))     #recebe a opção escolhida
        if (pergunta != 1):     #verifica se a opção é diferente de verdadeiro (aceitar)
            print('O valor total da conta é:R${:.2f}'.format(soma))     #exibe o(os) valor(es) total(is) a pagar
            print(d3)       #exibe o detalhe sobre os agradecimentos finais
            print('A Lanchonete RU3927883 agradece a preferência, volte sempre!')   #agradecimento final pela escolha da lanchonete
            print(d3)       #exibe o detalhe sobre os agradecimentos finais
            break   #pausa e finaliza a operação

    else:   #será iniciado esta função caso seja digitado um codigo invalido, diferente do cardapio
        print('Operação invalida! Digite um código válido.') #exibe a mensagem caso tenha digitado um codigo errado
        continue    #volta ao começo do laço caso tenha digitado um codigo de produto diferente do cardapio


























































