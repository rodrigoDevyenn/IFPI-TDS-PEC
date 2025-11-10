def conceito(n):
    if n >= 8.5:
        return 'A'
    elif n >= 7.0:
        return 'B'
    elif n >= 5.0:
        return 'C'
    elif n >= 4.0:
        return 'D'
    else:
        return 'E'

def main():
    while True:
        nota = float(input('Informe a nota do aluno: '))
        if nota >= 0 and nota <= 10:
            print(f'O resultado é {conceito(nota)}')
            break
        else:
            print('Nota inválida.')

if __name__ == '__main__':
    main()