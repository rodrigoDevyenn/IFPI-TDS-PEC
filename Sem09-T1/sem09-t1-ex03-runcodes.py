
def perimetroRetangulo(b, h):
    return (b * 2) + (h * 2)

def areaRetangulo(b, h):
    return b * h

def verifica(b, h):
    if b == h:
        return 'QUADRADO'
    else:
        resultado = f"{perimetroRetangulo(b, h):.0f} - {areaRetangulo(b, h):.0f}"
        return resultado

def main():
    
    base = float(input())
    altura = float(input())

    print(verifica(base, altura))

if __name__ == '__main__':
    main()