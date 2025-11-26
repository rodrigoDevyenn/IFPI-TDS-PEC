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
            valor = int(input())
            lista.append(valor)
        return lista
    else:
        lista = []
        for i in range(n):
            valor = int(input())
            lista.insert(0, valor)
        return lista

def main():
    
    n = int(input())

    print(preencherLista(n,'a'))
    print(preencherLista(n, 'b'))
    print(listaUsuario(n, 'c'))
    print(listaUsuario(n, 'd'))

if __name__ == '__main__':
    main()