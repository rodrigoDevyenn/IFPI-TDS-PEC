def par_ou_impar(n):
    if n % 2 == 0:
        return 'par'
    else:
        return 'ímpar'

def verifica(mod, n):
    if mod == 0:
        return (9 * n) + 7
    elif mod == 1:
        return par_ou_impar(n)
    elif mod == 2:
        return (5 * (n ** 2)) - (3 * n) + 42
    elif mod == 3:
        return n // 10
    elif mod == 4:
        return pow(n,2)

def main():

    num = int(input('Insira um número inteiro: '))
    mod = num % 5

    print(verifica(mod, num))

if __name__ == '__main__':
    main()
