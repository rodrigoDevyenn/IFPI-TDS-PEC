
def porcentagem(x, por):
    return x * (por / 100)

def previsao(a, b):
    contador = 0
    while b < a:
        a += porcentagem(a, 2)
        b += porcentagem(b, 3)
        contador += 1
    return contador

def main():
    popA = int(input())
    popB = int(input())
    if popA > popB:
        print(previsao(popA, popB))
    else:
        print(previsao(popB, popA))

if __name__ == '__main__':
    main()