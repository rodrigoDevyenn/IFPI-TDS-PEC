def menu():
    return 'CÓDIGO  PRODUTO         PREÇO (R$)\nH       Hamburger       5,50\nC       Cheeseburger    6,80\nM       Misto Quente    4,50\nA       Americano       7,00\nQ       Queijo Prato    4,00\nX       PARA TOTAL DA CONTA'

def escolha(op):
    if op == 'H':
        return 5.50
    elif op == 'C':
        return 6.80
    elif op == 'M':
        return 4.50
    elif op == 'A':
        return 7.00
    elif op == 'Q':
        return 4.00
    else:
        return 0.00

def main():
    soma = 0
    while True:
        print(menu())
        opcao = input().strip()
        if opcao == 'X':
            print(f'{soma:.2f}')
            break
        else:
            soma += escolha(opcao)
        

if __name__ == '__main__':
    main()