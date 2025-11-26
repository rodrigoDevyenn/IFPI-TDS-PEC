def ehPar(n):
    return n % 2 == 0

def listaParOuImpar(l):
    listaPar = []
    listaImpar = []
    for i in range(20):
        if ehPar(l[i]):
            listaPar.append(l[i])
        else:
            listaImpar.append(l[i])
    return listaPar, listaImpar

def main():

    Lista = []
    for i in range(20):
        num = int(input())
        Lista.append(num)
    
    Par, Impar = listaParOuImpar(Lista)
    print(Lista)
    print(Par)
    print(Impar)

if __name__ == '__main__':
    main()