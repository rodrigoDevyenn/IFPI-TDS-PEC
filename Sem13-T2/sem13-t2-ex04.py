def soma_cumulativa(l):
    listaCumulativa = []
    a = 0
    for i in range(len(l)):
        a += l[i]
        listaCumulativa.append(a)
    return listaCumulativa

def main():
    
    Lista = []
    c = 1
    print('Insira os números da Lista(Digite 0 para finalizar)!')
    while True:
        val = int(input(f'Insira o valor {c}: '))
        if val != 0:
            Lista.append(val)
            c += 1
        else:
            break
    print(soma_cumulativa(Lista))

if __name__ == '__main__':
    main()