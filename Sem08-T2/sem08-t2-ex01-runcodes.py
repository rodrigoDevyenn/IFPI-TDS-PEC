
def ehPar(n):
    return n % 2 == 0

def soma(n):
    if ehPar(n):
        return n + 5
    else:
        return n + 8

def main():

    num = int(input())
    print(soma(num))

if __name__ == '__main__':
    main()