
def ehImpar(n):
    return  n % 2 != 0

def digitosImpares(n):
    c = 0
    unidade  = n % 10
    dezena = n // 10
    if ehImpar(unidade):
        c += 1
    if ehImpar(dezena):
        c += 1
    return c

def contador(c):
    if c == 0:
        return "Nenhum dígito é ímpar."
    elif c == 1:
        return "Apenas um dígito é ímpar."
    else: 
        return "Os dois dígitos são ímpares."

def main():
    numero = int(input())
    print(contador(digitosImpares(numero)))

if __name__ == '__main__':
    main()