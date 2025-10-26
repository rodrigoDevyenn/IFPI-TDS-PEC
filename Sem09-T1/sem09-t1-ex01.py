
def comparaNumeros(a, b, c):
    if a == b and b == c:
        return 'Todos os valores são iguais'
    elif a != b and a != c and b != c:
        return 'Todos os valores são diferentes'
    else:
        return 'Existem dois valores iguais e um diferente'

def main():

    print('Insira 3 número inteiros: ')
    num_a = int(input('Primeiro número: '))
    num_b = int(input('Segundo número: '))
    num_c = int(input('Terceiro número: '))

    print(comparaNumeros(num_a, num_b, num_c))

if __name__ == '__main__':
    main()