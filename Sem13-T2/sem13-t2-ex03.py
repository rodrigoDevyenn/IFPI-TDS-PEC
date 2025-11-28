
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
    print('Insira as 50 notas na lista!')
    for i in range(50):
        nota = float(input(f'Insira a nota do {i+1}° aluno: '))
        Lista.append(nota)
    
    print(verificaNota(Lista))

if __name__ == '__main__':
    main()