def media(n, qtd):
    return n / qtd

def main():
    soma = 0
    cont = 0
    while True:
        num = int(input())
        if num != 0:
            soma = soma + num
            cont += 1
        else:
            break
    print(f'{media(soma, cont):.2f}')

if __name__ == '__main__':
    main()