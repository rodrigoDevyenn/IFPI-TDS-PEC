
def ehPar(n):
    return n % 2 == 0

def digitosPares(n):
    c = 0
    if len(str(n)) == 4:
        unidade = n % 10
        dezena = (n // 10) % 10
        centena = (n // 100) % 10
        milhar = n // 1000
        if ehPar(unidade):
            c += 1
        if ehPar(dezena):
            c += 1
        if ehPar(centena):
            c += 1 
        if ehPar(milhar):
            c += 1

    elif len(str(n)) == 3:
        unidade = n % 10
        dezena = (n // 10) % 10
        centena = n // 100
        if ehPar(unidade):
            c += 1
        if ehPar(dezena):
            c += 1
        if ehPar(centena):
            c += 1 

    elif len(str(n)) == 2:
        unidade = n % 10
        dezena = (n // 10) % 10
        if ehPar(unidade):
            c += 1
        if ehPar(dezena):
            c += 1
    return c
    
def main():
    numero = int(input('Insira o número: '))
    print(digitosPares(numero))

if __name__ == '__main__':
    main()