
def juntarLista(la,lb):
    ListaC = []
    for i in range(25):
        ListaC.append(la[i])
        ListaC.append(lb[i])
    return ListaC

def main():
    
    ListaA = []
    ListaB = []
    
    for i in range(25):
        num = int(input(f'Insira o número {i + 1}: '))
        ListaA.append(num)
    
    for i in range(25):
        num = int(input(f'Insira o número {i + 1}: '))
        ListaB.append(num)
    
    print('Lista A:')
    print(ListaA)
    print('Lista B:')
    print(ListaB)
    print('Lista C:')
    print(juntarLista(ListaA, ListaB))

if __name__ == '__main__':
    main()