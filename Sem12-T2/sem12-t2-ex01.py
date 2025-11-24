def fatorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

def main():
    numero = int(input('Insira um número: '))
    print(f'O fatorial de {numero} é {fatorial(numero)}.')

if __name__ == "__main__":
    main()