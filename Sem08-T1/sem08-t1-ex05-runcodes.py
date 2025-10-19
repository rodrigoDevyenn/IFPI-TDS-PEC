
def calculaIMC(p, h):
    return p / pow(h, 2)

def verificaIMC(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc >= 18.5 and imc < 25:
        return 'Peso normal'
    elif imc >= 25 and imc < 30:
        return 'Sobrepeso'
    elif imc >= 30 and imc < 35:
        return 'Obeso leve'
    elif imc >= 35 and imc < 40:
        return 'Obeso moderado'
    elif imc >= 40:
        return 'Obeso mórbido'

def main():

    peso = float(input())
    altura = float(input())

    print(calculaIMC(peso, altura))
    print(verificaIMC(calculaIMC(peso, altura)))

if __name__ == '__main__':
    main()