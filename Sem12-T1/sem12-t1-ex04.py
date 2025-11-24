
def numeroDaSorte(n):
    string = str(n)
    soma = 0
    for i in range(len(string)):
        soma += int(string[i])
    return soma

def main():
    print('=====NÚMERO=DA=SORTE=====')
    data_nasc = int(input('Insira sua data de nascimento(ddmmaaaa): '))
    print(f'Seu número da sorte é {numeroDaSorte(data_nasc)}!')

if __name__ == '__main__':
    main()