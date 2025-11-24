
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
    popA = int(input('Insira a população do país A: '))
    popB = int(input('Insira a população do país B: '))
    if popA > popB:
        print(f'A população do país B irá ultrapassar a população do país A em {previsao(popA, popB)} anos!')
    else:
        print(f'A população do país A irá ultrapassar a população do país B em {previsao(popB, popA)} anos!')

if __name__ == '__main__':
    main()