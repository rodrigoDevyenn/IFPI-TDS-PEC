def esta_ordenado(l):
    listaOrdenada = sorted(l)
    return listaOrdenada == l
        
def main():
    
    Lista = []
    n = int(input())
    for i in range(n):
        num = input().strip()
        if num.isalpha():
            Lista.append(num)
        else:
            Lista.append(float(num))
    
    if esta_ordenado(Lista):
        print('LISTA ORDENADA')
    else:
        print('LISTA NÃO ORDENADA')

if __name__ == '__main__':
    main()