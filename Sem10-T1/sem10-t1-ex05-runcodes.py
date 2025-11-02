
def ehMaior(n, m):
    if n > m:
        return n
    else:
        return m

def main():
    maior = 0
    for i in range(1, 101):
        num = int(input())
        maior = ehMaior(num, maior)
    print(maior)

if __name__ == '__main__':
    main()