
def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

def selecaoOperacao(x, y, op):
    if op == '1':
        return adicao(x, y)
    elif op == '2':
        return subtracao(x, y)
    elif op == '3':
        return multiplicacao(x, y)
    elif op == '4':
        return divisao(x, y)

def main():

    print('Insira os dois valores e em seguida a operação desejada:\n1 – Adição\n2 – Subtração\n3 – Multiplicação\n4 - Divisão')
    valor_a = float(input('Primeiro valor: '))
    valor_b = float(input('Segundo valor: '))
    operacao = input('Operação: ').strip()

    print(selecaoOperacao(valor_a, valor_b, operacao))

if __name__ == '__main__':
    main()