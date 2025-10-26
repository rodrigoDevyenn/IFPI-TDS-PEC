
def subtracao(x, y):
    return x - y

def comparaDiferenca(a, b, c):
    segundo = subtracao(a, b)
    terceiro = subtracao(a, c)
    if segundo < terceiro:
        return f'{b}\n{segundo}'
    else:
        return f'{c}\n{terceiro}'

def main():
    
    print('Insira 3 números inteiros:')
    num_a = int(input('Primeiro número: '))
    num_b = int(input('Segundo número: '))
    num_c = int(input('Terceiro número: '))

    print(comparaDiferenca(num_a, num_b, num_c))

if __name__ == '__main__':
    main()