
def ehMaior(m, n):
    if verificaZero(n):
        if n > m:
            return n

def verificaZero(n):
    return n != 0

def verificaValorNulo(m, n):
    return ehMaior(m, n) != None

def main():
    aux = 0
 
    numA = int(input('Primeiro número: '))
    numB = int(input('Segundo número: '))
    numC = int(input('Terceiro número: '))
    numD = int(input('Quarto número: '))
    numE = int(input('Quinto número: '))

    m = (numA + numB + numC + numD + numE) / 5
    print(f'{m:.2f}')
    
    
    if verificaValorNulo(m, numA):
        print(ehMaior(m, numA))
    if verificaValorNulo(m, numB):
        print(ehMaior(m, numB))
    if verificaValorNulo(m, numC):
        print(ehMaior(m, numC))
    if verificaValorNulo(m, numD):
        print(ehMaior(m, numD))
    if verificaValorNulo(m, numE):
        print(ehMaior(m, numE))

if __name__ == '__main__':
    main()