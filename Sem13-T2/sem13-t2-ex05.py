def esta_ordenado(l):
    listaOrdenada = sorted(l)
    return listaOrdenada == l
        
def main():
    
    Lista = []
    n = int(input('Insira quantos elementos terá a lista: '))
    for i in range(n):
        num = input(f'Insira o elemento {i+1}: ').strip()
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