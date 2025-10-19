
def pesoIdeal(s, h):
    if s == 1:
        return (72.7 * h) - 58
    else:
        return (62.1 * h) - 44.7

def main():

    altura = float(input('Altura: '))
    sexo = int(input('Sexo(1 - Masculino, 2 - Feminino): '))

    print(f'{pesoIdeal(sexo, altura):.2f}')

if __name__ == '__main__':
    main()
