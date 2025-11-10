
def aumentoPercentual(v, p):
    return (v * (p/100))

def evolucao(s, d):
    mes = 10
    ano = 2016
    while True:
        if mes < 12:
            mes += 1
        else:
            mes = 1
            ano += 1
        print(f'Data: {mes}/{ano}')
        d = d + aumentoPercentual(d, 15)
        if mes == 3:
            s = s + aumentoPercentual(s, 5)
        print(f'Salário: {s:.2f}')
        print(f'Dívida: {d:.2f}\n')
        if d > s:
            break
    return f'{mes}/{ano}'

def main():
    print('Data: 10/2016')
    print('Quando a dívida de Pedro será superior ao seu salário, sabendo que seu salário\naumenta 5% todo ano no mês de março e sua dívida aumenta em 15% todo mês?')
    salario = float(input('Insira o salário de Pedro: '))
    divida = float(input('Insira o valor da dívida de Pedro: \n'))

    print(f'Isso acontecera em {evolucao(salario, divida)}!')

if __name__ == '__main__':
    main()