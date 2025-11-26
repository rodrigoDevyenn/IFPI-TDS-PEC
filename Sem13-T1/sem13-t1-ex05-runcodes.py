
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
        num = int(input())
        ListaA.append(num)
    
    for i in range(25):
        num = int(input())
        ListaB.append(num)
    
    print(ListaA)
    print(ListaB)
    print(juntarLista(ListaA, ListaB))

if __name__ == '__main__':
    main()