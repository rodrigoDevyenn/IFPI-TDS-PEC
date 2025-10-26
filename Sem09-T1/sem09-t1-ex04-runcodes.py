
def subtracao(x, y):
    return abs(x - y)

def comparaDiferenca(a, b, c):
    segundo = subtracao(a, b)
    terceiro = subtracao(a, c)
    if segundo < terceiro:
        return segundo
    else:
        return terceiro

def main():
    
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())

    print(comparaDiferenca(num_a, num_b, num_c))

if __name__ == '__main__':
    main()