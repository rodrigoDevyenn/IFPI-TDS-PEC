def formatarCasas(n):
    string = f'{n:.4f}'
    return float(string)
    
def valoresInversos(n):
    lista = []
    for i in range(n):
        num = float(input())
        lista.insert(0, formatarCasas(num))
    return lista

def notas(n):
    lista = []
    soma = 0
    for i in range(n):
        nota = float(input())
        lista.append(nota)
    return lista

def media(l):
    if len(l) == 0:
        return 'SEM NOTAS'
    else:
        return f'{sum(l) / len(l):.1f}'

def listaLetras(n):
    lista = []
    v = 0
    for i in range(n):
        letra = input().strip()
        if ehVogal(letra):
            v += 1
        else:
            lista.append(letra)
    return v, lista
        
def ehVogal(s):
    return s.upper() in ('A', 'E', 'I', 'O', 'U')

def main():
    
    n = int(input())

    print(valoresInversos(n))

    listaNotas = notas(n)
    print(listaNotas)
    print(media(listaNotas))

    qtd_vogais, consoantes = listaLetras(n)
    print(qtd_vogais)
    print(consoantes)
    
if __name__ == '__main__':
    main()