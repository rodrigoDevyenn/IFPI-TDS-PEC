def menu():
    return 'OPÇÕES:\n1 - SAUDAÇÃO\n2 - BRONCA\n3 - FELICITAÇÃO\n0 - FIM'

def escolha(op):
    if op == '1':
        return '1 - Olá. Como vai?'
    elif op == "2":
        return '2 - Vamos estudar mais.'
    elif op == '3':
        return '3 - Meus Parabéns!'
    elif op == '0':
        return '0 - Fim de serviço.'
    else:
        return 'Opção inválida.'

def main():
    while True:
        print(menu())
        opcao = input().strip()
        print(escolha(opcao))
        if opcao == '0':
            break

if __name__ == '__main__':
    main()