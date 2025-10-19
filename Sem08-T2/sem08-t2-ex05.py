
def mediaFinal(a, b, c, m):
    return ((a + b * 2) + (c * 3 + m)) / 7

def conceito(m):
    if m >= 9.0:
        return 'A'
    elif m >= 7.5 and m < 9.0:
        return 'B'
    elif m >= 6.0 and m < 7.5:
        return 'C'
    elif m >= 4.0 and m < 6.0:
        return 'D'
    elif m < 4.0:
        return 'E'
    
def resultado(mat, a, b, c, m):
    mediaf = mediaFinal(a, b, c, m)
    conc = conceito(mediaf)

    if conc == 'A' or conc == 'B' or conc == 'C':
        return f'{mat}\n{mediaf:.2f}\n{conc}\nAprovado'
    else:
        return f'{mat}\n{mediaf:.2f}\n{conc}\nReprovado'
    

def main():
    
    matricula = input('Matrícula')
    notaA = float(input('Nota 1: '))
    notaB = float(input('Nota 2: '))
    notaC = float(input('Nota 3: '))
    media = float(input('Média dos Exercícios: '))

    print(resultado(matricula, notaA, notaB, notaC, media))

if __name__ == '__main__':
    main()