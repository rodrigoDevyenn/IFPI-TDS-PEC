
def verificaNota(l):
    listaIndice = []
    for i in range(50):
        if l[i] >= 6:
            listaIndice.append(i)
        else:
            continue
    return listaIndice

def main():
    
    Lista = []
    for i in range(50):
        nota = float(input())
        Lista.append(nota)
    
    print(verificaNota(Lista))

if __name__ == '__main__':
    main()