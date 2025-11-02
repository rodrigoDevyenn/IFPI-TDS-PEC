
def ehMaior(n, m):
    if n > m:
        return n
    else:
        return m

def main():
    maior = 0
    print('Insira um conjunto de 100 números inteiros:')
    for i in range(1, 101):
        num = int(input(f'Insira o número {i+1}º: '))
        maior = ehMaior(num, maior)
    print(maior)

if __name__ == '__main__':
    main()