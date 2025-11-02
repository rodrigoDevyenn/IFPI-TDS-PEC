def loop(c):
    for i in range(1,25):
        print(f'{i}x de R$ {prestacao(c,i):.2f} ')

def prestacao(c, np):
    return c / np

def main():
    compra = float(input('Informe o valor da compra: '))
    loop(compra)

if __name__ == '__main__':
    main()