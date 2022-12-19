from matplotlib import pyplot as plt    # Importação da biblioteca


def operacao(x, a, b, c):   # Realiza a operação e mostra os resultados de y1,y2 e y3
    y = a * x + b * x - c
    return y


x1 = 10     # Valores pré defindos de x1, x2 e x3
x2 = 8
x3 = 15

a = 8       # Valores definidos de a,b, e c pelos últimos três digitos do meu RU
b = 8
c = 3

plt.title('equação a*x + b*x - c')  # Insere o titúlo no gráfico

plt.grid()      # Insere acabamento interno de grade quadriculada
plt.xlabel('eixo x')    # Define o noem do eixo x
plt.ylabel('eixo y')    # Define o noem do eixo y

plt.plot(x1, operacao(x1, a, b, c), marker='o', markersize=10, markerfacecolor='yellow')    # Realiza o plot do eixo x e y
plt.plot(x2, operacao(x2, a, b, c), marker='o', markersize=10, markerfacecolor='green')
plt.plot(x3, operacao(x3, a, b, c), marker='o', markersize=10, markerfacecolor='blue')

    # Insere a legenda dos valores no gráfico
plt.legend( [f'x={x1} y={operacao(x1, a, b, c)}', f'x={x2} y={operacao(x2, a, b, c)}', f'x={x3} y={operacao(x3, a, b, c)}'])


plt.show() #Exibe o gráfico

