
def eh_impar(n):
    return n % 2 != 0

def main():
    
    numero = int(input('Insira o número: '))
    print(eh_impar(numero))

if __name__ == '__main__':
    main()