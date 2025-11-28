
def ordenacao(l):
    return sorted(l)

def ehPar(n):
    return n % 2 == 0

def multiplica(l):
    lista = []
    for i in range(100):
        if ehPar(i):
            lista.append(l[i] * 3)
        else:
            lista.append(l[i] * 5)
    return lista

def main():
    
    Lista = []
    print('Insira os números na lista!')
    for i in range(100):
        num = int(input(f'Insira o número {i+1}: '))
        Lista.append(num)
    
    lista_ordenada = ordenacao(Lista)
    print(multiplica(lista_ordenada))
    

if __name__ == '__main__':
    main()