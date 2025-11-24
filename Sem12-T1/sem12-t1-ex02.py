def porcentagem(x, por):
    return x * (por / 100)

def planejamento(c):
    p = 10000
    contador = 0
    while p < c:
        p += porcentagem(p, 0.7)
        c += porcentagem(c, 0.4)
        contador += 1
    return contador 

def main():
    carro = float(input('Insira o valor do carro hoje: '))
    print(f'Você poderá comprar o carro à vista em {planejamento(carro)} meses!')

if __name__ == '__main__':
    main()