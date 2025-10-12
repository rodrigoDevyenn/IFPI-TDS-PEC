
def pontoExtra(n3):
    return n3 > 8

def media(n1, n2, n3):
    if pontoExtra(n3):
        return ((n1 + n2 +n3) / 3) + 1
    else:
        return (n1 + n2 + n3) / 3

def verificaMediaAcima(m):
    if m > 10:
        return  10
    else:
        return m

def main():

    nota1 = float(input('Insira a primeira nota: '))
    nota2 = float(input('Insira a segunda nota: '))
    nota3 = float(input('Insira a terceira nota: '))

    print(verificaMediaAcima(media(nota1, nota2, nota3)))


if __name__ == '__main__':
    main()