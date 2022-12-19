class calculadora:      # Cria-se a Classe Calculadora

    def __int__(self):      # Metodo construtor que se inicia a classe
        self.numru01 = 0    # Atributo número 01 recebe o valro inicial zero
        self.numru02 = 0    # Atributo número 02 recebe o valro inicial zero
        self.valorfinal = 0     # Atributo do resultado recebe o valor inicial zero

    def soma(self, numru01, numru02):   # Método que irá realizar a soma dos dois valores
        self.numru01 = numru01          # Primeiro valor recebe ele mesmo
        self.numru02 = numru02          # Segundo valor recebe ele mesmo
        self.valorfinal = self.numru01 + self.numru02           # Valor final realiza e mostra o resultado final da operação através do próximo "return"

        return self.valorfinal

    def subtracao(self, numru01, numru02):      # Método que irá realizar a subtração dos dois valores
        self.numru01 = numru01                              # Primeiro valor recebe ele mesmo
        self.numru02 = numru02                              # Segundo valor recebe ele mesmo
        self.valorfinal = self.numru01 - self.numru02       # Valor final realiza e mostra o resultado final da operação através do próximo "return"

        return self.valorfinal

    def multiplicacao(self, numru01, numru02):      # Método que irá realizar a multiplicação dos dois valores
        self.numru01 = numru01                          # Primeiro valor recebe ele mesmo
        self.numru02 = numru02                              # Segundo valor recebe ele mesmo
        self.valorfinal = self.numru01 * self.numru02           # Valor final realiza e mostra o resultado final da operação através do próximo "return"

        return self.valorfinal

    def divisao(self, numru01, numru02):    # Método que irá realizar a divisão dos dois valores
        self.numru01 = numru01                  # Primeiro valor recebe ele mesmo
        self.numru02 = numru02                              # Segundo valor recebe ele mesmo
        self.valorfinal = self.numru01 / self.numru02           # Valor final realiza e mostra o resultado final da operação através do próximo "return"

        return self.valorfinal

    def expoente(self, numru01, numru02):   # Método que irá realizar o expoente dos dois valores
        self.numru01 = numru01              # Primeiro valor recebe ele mesmo
        self.numru02 = numru02                              # Segundo valor recebe ele mesmo
        self.valorfinal = self.numru01 ** self.numru02          # Valor final realiza e mostra o resultado final da operação através do próximo "return"

        return self.valorfinal

    def restodivisao(self, numru01, numru02):       # Método que irá realizar o resto da divisão dos dois valores
        self.numru01 = numru01                      # Primeiro valor recebe ele mesmo
        self.numru02 = numru02                              # Segundo valor recebe ele mesmo
        self.valorfinal = self.numru01 % self.numru02           # Valor final realiza e mostra o resultado final da operação através do próximo "return"

        return self.valorfinal

def prosseguir(inicio):         # Cria-se uma função que tem o objetivo de permitir o usuário fazer mais operações ou finalizar o processo
    if inicio:
        return True
    else:
        return False

def menu():                         # Cria-se a Função que exibe o menu de opções
    opcao = {1: 'Somar',
             2: 'Subtrair',
             3: 'Multiplicar',
             4: 'Dividir',
             5: 'Expoente',
             6: 'Resto da Divisão'}

    ini_calc = calculadora()        # Método que inicia a classe calculadora com seus métodos

    det = '-' * 90
    print(det)
    print("""Selecione a operação que deseja realizar:
         
    1 - Somar
    2 - Subtrair
    3 - Multiplicar
    4 - Dividir
    5 - Expoente
    6 - Resto da Divisão
    
    >> Digite o número relacionado com a operação que deseja realizar e pressione ENTER <<""")      # Exibe as opções dispiniveis para o usuário
    print(det)

    calculo = True
    while calculo:      # Cria-se um laço de repetição com intuito de instruir o usuário a selecionar apenas as opções dispinveis

        print("Qual operação deseja realizar? (1,2,3,4,5,6)")
        escolha = input('>>')
        if not (escolha in '1 2 3 4 5 6'):
            print("Opção Inválida!! Por favor, escolha uma opção válida do menu.")      # Se a condição do laço de repetição não for satisfeita exibe este aviso
            continue

        else:
            escolha = int(escolha)      # Define que a variavel receba números inteiros
            print(f"A operação escolhida foi:{opcao[escolha]}.")        # Exibe a opção selecionada
            print(">> Apenas números inteiros serão permitidos <<")         # Aviso para somente inserir números inteiros

        if escolha == 1:
            valor1 = int(input("Digite o penúltimo digito do seu RU:"))     # Entrada do penúltimo digito do RU
            valor2 = int(input("Digite o último digito do seu RU:"))        # Entrada do último digito do RU
            resultado = ini_calc.soma(valor1, valor2)       # Inicia a operação com os dois valores inseridos
            print(f"O resultado é:{resultado}")     # Exibe o resultado da operação
            calculo = prosseguir(input("Pressione qualquer tecla para continuar ou pressione ENTER para finalizar."))

        elif escolha == 2:
            valor1 = int(input("Digite o penúltimo digito do seu RU:"))     # Entrada do penúltimo digito do RU
            valor2 = int(input("Digite o último digito do seu RU:"))        # Entrada do último digito do RU
            resultado = ini_calc.subtracao(valor1, valor2)          # Inicia a operação com os dois valores inseridos
            print(f"O resultado é:{resultado}")     # Exibe o resultado da operação
            calculo = prosseguir(input("Pressione qualquer tecla para continuar ou pressione ENTER para finalizar."))

        elif escolha == 3:
            valor1 = int(input("Digite o penúltimo digito do seu RU:"))     # Entrada do penúltimo digito do RU
            valor2 = int(input("Digite o último digito do seu RU:"))            # Entrada do último digito do RU
            resultado = ini_calc.multiplicacao(valor1, valor2)          # Inicia a operação com os dois valores inseridos
            print(f"O resultado é:{resultado}")     # Exibe o resultado da operação
            calculo = prosseguir(input("Pressione qualquer tecla para continuar ou pressione ENTER para finalizar."))

        elif escolha == 4:
            valor1 = int(input("Digite o penúltimo digito do seu RU:"))         # Entrada do penúltimo digito do RU
            valor2 = int(input("Digite o último digito do seu RU:"))            # Entrada do último digito do RU
            resultado = ini_calc.divisao(valor1, valor2)            # Inicia a operação com os dois valores inseridos
            print(f"O resultado é:{resultado}")         # Exibe o resultado da operação
            calculo = prosseguir(input("Pressione qualquer tecla para continuar ou pressione ENTER para finalizar."))

        elif escolha == 5:
            valor1 = int(input("Digite o penúltimo digito do seu RU:"))     # Entrada do penúltimo digito do RU
            valor2 = int(input("Digite o último digito do seu RU:"))        # Entrada do último digito do RU
            resultado = ini_calc.expoente(valor1, valor2)           # Inicia a operação com os dois valores inseridos
            print(f"O resultado é:{resultado}")     # Exibe o resultado da operação
            calculo = prosseguir(input("Pressione qualquer tecla para continuar ou pressione ENTER para finalizar."))

        elif escolha == 6:
            valor1 = int(input("Digite o penúltimo digito do seu RU:"))     # Entrada do penúltimo digito do RU
            valor2 = int(input("Digite o último digito do seu RU:"))        # Entrada do último digito do RU
            resultado = ini_calc.restodivisao(valor1, valor2)               # Inicia a operação com os dois valores inseridos
            print(f"O resultado é:{resultado}")     # Exibe o resultado da operação
            calculo = prosseguir(input("Pressione qualquer tecla para continuar ou pressione ENTER para finalizar."))


menu()
