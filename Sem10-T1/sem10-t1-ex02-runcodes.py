
def ehPar(n):
    return n % 2 == 0

def contadorPar(x):
    if x == True:
        return 1
    else:
        return 0

def contadorImpar(x):
    if x == True:
        return 0
    else:
        return 1

def main():
    par = 0
    impar = 0
    for i in range(100):
        num = int(input())
        par = par + contadorPar(ehPar(num))
        impar = impar + contadorImpar(ehPar(num))

    print(par)
    print(impar)

if __name__ == '__main__':
    main()