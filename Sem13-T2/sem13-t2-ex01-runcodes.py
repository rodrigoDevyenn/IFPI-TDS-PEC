
def multiplica_constante(l, c):
    lista_mult = []
    for i in range(len(l)):
        lista_mult.append(l[i] * c)
    return lista_mult

def main():
    
    Lista = []
    while True:
        n = int(input())
        if n != 0:
            Lista.append(n)
        else:
            break
    constante = int(input())

    print(multiplica_constante(Lista, constante))

if __name__ == '__main__':
    main()