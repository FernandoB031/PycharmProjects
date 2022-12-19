def calculadoraIMC():

    print("""Tabela de instruções do resultado médio pelo mundo e no Brasil:
    
    - 16 a 16,5 Kg/m² - Muito abaixo do peso
    - 17 a 18,4 Kg/m² - Abaixo do peso
    - 18,5 a 24,9 Kg/m² - Peso normal
    - 25 a 29,9 Kg/m² - Acima do peso
    - 30 a 34,9 Kg/m² - Obesidade grau 1
    - 35 a 40 Kg/m² - Obesidade grau 2
    - Maior que 40 Kg/m² - Obesidade grau 3
    
    >> O resultado vai indicar a faixa que o indivíduo se encontra e quais os possíveis
    riscos e impactos na saúde.<<""")


    d1 = '|'
    d2 = '-' * 32
    print(d2)
    print(d1 + 'Digite seu peso (Kilos,ex:45):' + d1)
    print(d2)
    peso = int(input('>>'))

    d3 = '-' * 37
    print(d3)
    print(d1 + 'Digite sua altura (metros,ex:1.60):' + d1)
    print(d3)
    altura = float(input('>>'))


    altura **= 2
    resultado = peso / altura

    d4 = '-' *27
    print(d4)
    print(d1 + 'Seu IMC atual é de: {:.2f}' .format(resultado) +d1)
    print(d4)

    if (resultado >= 10 and resultado <= 16.5):
        det2 = '#' *108
        print(det2)
        print(d1 + 'Você pode estar muito abaixo do peso, recomenda-se procurar um médico especialista para entender o motivo.' + d1)
        print(det2)

    elif (resultado >= 17 and resultado <= 18.4):
        det2 = '#' *102
        print(det2)
        print(d1 + 'Você pode estar abaixo do peso, recomenda-se procurar um especialista médico para entender o motivo.' + d1)
        print(det2)

    elif (resultado >= 18.5 and resultado <= 24.9):
        det2 = '#' *51
        print(det2)
        print(d1 + 'Você está no peso normal segundo suas proporções.' + d1)
        print(det2)

    elif (resultado >= 25 and resultado <= 29.9):
        det2 = '#' *102
        print(det2)
        print(d1 + 'Você pode estar acima do peso, recomenda-se procurar um especialista médico para entender o motivo. ' + d1)
        print(det2)

    elif (resultado >= 30 and resultado <= 34.9):
        det2 = '#' *73
        print(det2)
        print(d1 + 'Você pode estar com obesidade de grau 1, procure um especialista médico' + d1)
        print(det2)

    elif (resultado >= 35 and resultado <= 40):
        det2 = '#' *73
        print(det2)
        print(d1 + 'Você pode estar com obesidade de grau 2, procure um especialista médico'+ d1)
        print(det2)

    elif (resultado >= 40):
        det2 = '#' *73
        print(det2)
        print(d1 + 'Você pode estar com obesidade de grau 3, procure um especialista médico'+ d1)
        print(det2)



    print("""
    "Se você pratica qualquer tipo de esporte de alto rendimento ou treinamento resistivo com peso,
    estes valores apresentados, sendo eles para mais ou para menos, podem estar corretos considerando
    sua quantidade de massa magra atual. Sempre procure um médico para sua correta avaliação fisica."
    """)

    det3 = '-' *27
    print(det3)
    print(d1 + 'Calculadora finalizada...' + d1)
    print(det3)

calculadoraIMC()




