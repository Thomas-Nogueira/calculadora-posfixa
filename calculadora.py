
#Classe ciradora da Pilha para armazanamento dos valores.
class Pilha():

    def __init__(self):
        self.valores = []
    def vazia(self):
        return self.valores == []
    def topo(self):
        return self.valores[len(self.valores)-1]
    def tamanho(self):
        return len(self.valores)
    def empilha(self, e):
        self.valores.append(e)
    def desempilha(self):
        return self.valores.pop()


class Calculadora():

    #Variavel global
    expressao = Pilha()
    num = 0

    #Laço para armazenamento dos valores na pilha.
    for i in range(2):
        print('Digite um valor: ')
        expressao.empilha(input())

    #Escolher a operação aritmética.
    print('Digite a operação matemática: ')
    expressao.empilha(input())

    if expressao.topo() == '':
        print('Campo não pode ser vazio.')
        exit()
    else:

        if expressao.topo() == '+' or expressao.topo() == '-' or expressao.topo() == '*' or expressao.topo() == '/':
            #Se o ultimo elemento for o sinal de +.
            if expressao.topo() == '+':
                expressao.desempilha()
                for i in expressao.valores:
                    if type(i) is str:
                        print('Letras não são aceitas.')
                    break
                    num += float(i)
                print('Resultado = ', num)

            # Se o ultimo elemento for o sinal de -.
            if expressao.topo() == '-':
                expressao.desempilha()
                for i in expressao.valores:
                    if type(i) is str:
                        print('Letras não são aceitas.')
                    break
                    num += float(i)
                exit()
                num = num - float(expressao.topo()) * 2
                print('Resultado = ', num)

            # Se o ultimo elemento for o sinal de /.
            if expressao.topo() == '/':
                expressao.desempilha()
                for i in expressao.valores:
                    if type(i) is str:
                        print('Letras não são aceitas.')
                    break
                    num += float(i)
                exit()
                num = (num - float(expressao.topo())) / float(expressao.topo())
                print('Resultado = ', num)

            # Se o ultimo elemento for o sinal de *.
            if expressao.topo() == '*':
                expressao.desempilha()
                for i in expressao.valores:
                    if type(i) is str:
                        print('Letras não são aceitas.')
                    break
                    num += float(i)
                exit()
                num = (num - float(expressao.topo())) * float(expressao.topo())
                print('Resultado = ', num)
        else:
            print('Operação inválida.')
