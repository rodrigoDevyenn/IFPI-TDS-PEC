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
    num = int(input('Insira um número: '))
    print(eh_primo(num))

if __name__ == "__main__":
    main()