
def multiplica_constante(l, c):
    lista_mult = []
    for i in range(len(l)):
        lista_mult.append(l[i] * c)
    return lista_mult

def main():
    
    Lista = []
    cont = 1
    print('Insira os números da Lista(Digite 0 para finalizar!)')
    while True:
        n = int(input(f'Insira o número {cont}: '))
        if n != 0:
            Lista.append(n)
            cont += 1
        else:
            break
    constante = int(input('Insira a constante que será multiplicada: '))

    print(multiplica_constante(Lista, constante))

if __name__ == '__main__':
    main()