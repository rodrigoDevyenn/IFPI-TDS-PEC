def corrida(t):
    l = 0
    contador = 0
    while l < t:
        t += 1
        l += 10
        contador += 1
    return contador

def main():
    tartaruga = float(input('Insira quantos metros a tartaruga sairá na frente da lebre: '))
    print(f'A lebre levará {corrida(tartaruga)} minutos para alcançar a tartaruga!')


if __name__ == '__main__':
    main()