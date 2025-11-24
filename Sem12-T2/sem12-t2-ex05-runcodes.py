def eh_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def main():
    x = int(input('Insira o número x: '))
    y = int(input('Insira o número y: '))

    if x > y:
        x, y = y, x

    for num in range(x, y + 1):
        if eh_primo(num):
            print(num)


if __name__ == "__main__":
    main()