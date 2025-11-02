
def media(s):
    return s / 100

def main():
    soma = 0 
    print('Insira um conjunto de 100 números inteiros:')
    for i in range(100):
        num = int(input(f'Insira o número {i+1}º: '))
        soma = soma + num
    print(f'{media(soma):.2f}')
    

if __name__ == '__main__':
    main()
        