
def calcula(val, tax):
    return val + (val  * tax/100)

def evolucao(d, t):
    ano = 0
    valor = d
    while valor < (d * 2):
        valor = calcula(valor, t)
        ano += 1
    return ano

def main():
    
    print('Em quantos anos o valor do depósito será o dobro?')
    deposito = float(input('Insira o valor do depósito: \n'))
    taxa = float(input('Insira a taxa: '))
    
    print(f'R${deposito:.2f} rendendo {taxa:.0f}% ao ano irá dobrar em {evolucao(deposito, taxa)} anos.')

if __name__ == '__main__':
    main()