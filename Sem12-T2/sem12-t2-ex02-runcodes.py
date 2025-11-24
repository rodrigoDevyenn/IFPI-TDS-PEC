def fibonacci(n):
    p = 0
    s = 1
    contador = 0
    sequencia = '0, 1, '
    while True:
        f  = p + s
        contador += 1
        if contador == n - 2:
            sequencia += f'{str(f)}'
            break
        else:
            sequencia += f'{str(f)}, '
        p = s
        s = f
    return sequencia

def main():
    num = int(input())
    print(fibonacci(num))

if __name__ == "__main__":
    main()