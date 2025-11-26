def multiplicar(l):
    m = 1
    for i in range(10):
        m *= l[i]
    return m

def somar(l):
    s = 0
    for i in range(10):
        s += l[i]
    return s

def main():

    Lista = []
    for i in range(10):
        n = int(input(f'Insira o número {i + 1}: '))
        Lista.append(n)
    
    print(Lista)
    print(somar(Lista))
    print(multiplicar(Lista))

if __name__ == '__main__':
    main()