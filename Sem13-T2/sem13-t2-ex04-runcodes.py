def soma_cumulativa(l):
    listaCumulativa = []
    a = 0
    for i in range(len(l)):
        a += l[i]
        listaCumulativa.append(a)
    return listaCumulativa

def main():
    
    Lista = []
    while True:
        val = int(input())
        if val != 0:
            Lista.append(val)
        else:
            break
    print(soma_cumulativa(Lista))

if __name__ == '__main__':
    main()