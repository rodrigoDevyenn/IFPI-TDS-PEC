
def diaDaSemana(d):
    if d == '1':
        return 'domingo'
    elif d == '2':
        return 'segunda-feira'
    elif d == '3':
        return 'terça-feira'
    elif d == '4':
        return 'quarta-feira'
    elif d == '5':
        return 'quinta-feira'
    elif d == '6':
        return 'sexta-feira'
    elif d == '7':
        return 'sábado'
    else:
        return 'valor inválido'

def main():

    dia = input('Insira um número: ')
    print(diaDaSemana(dia))
    
if __name__ == '__main__':
    main()