
def converteEscala(l):
    escA = l[0][1]
    escB = l[1][1]

    if escA == escB:
        return l[0][0], l[1][0] 
    else:
        if l[0][1] == 'C':
            temA = l[0][0]
            temB = (l[1][0] - 32) * 5/9
        else:
            temA = (l[0][0] - 32) * 5/9
            temB = l[1][0]
        return temA, temB

def comparaTemperatura(l):
    temA, temB = converteEscala(l)
    if temA > temB:
        return l[0]
    elif temB > temA:
        return l[1]
    else:
        return 'Iguais'

def main():
    Lista = []
    for i in range(2):
        temperatura = float(input())
        escala = str(input()).upper()[0]
        Lista.append((temperatura, escala))
    
    print(comparaTemperatura(Lista))
    


if __name__ == '__main__':
    main()