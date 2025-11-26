def preencherLista(n, m):
    if m == 'a':
        lista = [0] * n
        return lista
    else:
        lista = []
        for i in range(n):
            lista.append(i + 1)
        return lista
    
def listaUsuario(n, m):
    if m == 'c':
        lista = []
        for i in range(n):
            valor = int(input(f'Insira o valor {i + 1}:'))
            lista.append(valor)
        return lista
    else:
        lista = []
        for i in range(n):
            valor = int(input(f'Insira o valor {i + 1}:'))
            lista.insert(0, valor)
        return lista

def main():
    
    n = int(input('Insira o tamanho das listas: '))

    print('Lista A')
    print(preencherLista(n,'a'))
    print('Lista B')
    print(preencherLista(n, 'b'))
    print('Lista C')
    print(listaUsuario(n, 'c'))
    print('Lista D')
    print(listaUsuario(n, 'd'))

if __name__ == '__main__':
    main()