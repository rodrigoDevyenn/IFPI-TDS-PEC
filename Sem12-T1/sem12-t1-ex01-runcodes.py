def corrida(t):
    l = 0
    contador = 0
    while l < t:
        t += 1
        l += 10
        contador += 1
    return contador

def main():
    tartaruga = float(input())
    print(corrida(tartaruga))


if __name__ == '__main__':
    main()