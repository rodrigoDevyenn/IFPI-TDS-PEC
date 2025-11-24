def calcula(n):
    i = 1
    h = 0
    while True:
        h += (1 / i)
        i += 1
        if i > n:
            break
    return h

def main():
    num = int(input('Insira N: '))
    print(f'{calcula(num):.4f}')

if __name__ == "__main__":
    main()