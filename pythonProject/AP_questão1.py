4det = '-' * 80                                                    #Pequeno acabamento sobre o inicio do programa
print(det)
print('Bem-Vindo a Loja de vendas em atacado RU3927883')          #Boas-vindas do programa
det = '-' * 80                                                    #Pequeno acabamento sobre o inicio do programa
print(det)

valor_unt = float(input('Digite o valor unitário do produto:'))   #Recebe o valor unitário do produto
quantidade = int(input('Digite a quantidade do produto:'))        #Recebe a quantidade de produtos

valor_final = valor_unt * quantidade                              #Calculo do valor bruto
desc1 = 1                                                         #Desconto sobre até 9 unidades
desc5 = valor_final * (5 / 100)                                   #Desconto entre 10 e 99 unidades
desc10 = valor_final * (10 / 100)                                 #Desconto entre 100 e 999 unidades
desc15 = valor_final * (15 /100)                                  #Desconto sobre mais de 1000 unidades

if (quantidade <= 9):                                  #Se a quantidade for até 9 produtos, este calculo será realizado
 preco = valor_final * desc1
 porc = 'com desconto de 0%'

elif (quantidade >= 10) and (quantidade <= 99):        #Se a quantidade for entre 10 e 99, este calculo será realizado
 preco = valor_final - desc5
 porc = 'com desconto de 5%'

elif (quantidade >= 100) and (quantidade <= 999):      #Se a quantidade for entre 100 e 999, este calculo será realizado
 preco = valor_final - desc10
 porc = 'com desconto de 10%'

else:                                                #Se a quantidade for 1000 ou maior, este calculo será realizado
    if (quantidade >= 1000):
     preco = valor_final - desc15
     porc = 'com desconto de 15%'

print('Valor total: R${:.2f}'.format(valor_final))                #Exibe o valor total bruto da compra
print('Valor total a ser pago: R${:.2f} {}'.format(preco, porc))  #Exibe o valor total a se pagar com o devido desconto


det = '-' * 80                                                    #Pequeno acabamento sobre o inicio do programa
print(det)
print('A loja RU3927883 agradece a preferência, volte sempre! Programa finalizado.')  #Agradecimentos finais pela compra
det = '-' * 80                                                    #Pequeno acabamento sobre o inicio do programa
print(det)


