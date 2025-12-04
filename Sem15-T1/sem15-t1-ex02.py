
def cParaF(t):
    return (t * 9/5) + 32

def fParaC(t):
    return (t - 32) * 5/9

def somarTemperaturas(l):
    tempA = l[0][0]
    tempB = l[1][0]
    escA = l[0][1]
    escB = l[1][1]
    if escA == escB:
        return tempA + tempB
    else:
        if escB == 'F':
            return cParaF(tempA) + tempB
        else:
            return fParaC(tempA) + tempB 


def escalaTemperatura(l):
    escA = l[0][1]
    escB = l[1][1]
    if escA == escB:
        return escA
    else:
        return escB

def main():
    Lista = []
    for i in range(2):
        temperatura = float(input(f'Insira a {i + 1}° temperatura: '))
        escala = str(input(f'Insira a {i + 1}° escala: ')).upper()[0]
        Lista.append((temperatura, escala))

    resultado = (round(somarTemperaturas(Lista), 4), escalaTemperatura(Lista))
    print(resultado)
    
if __name__ == '__main__':
    main()