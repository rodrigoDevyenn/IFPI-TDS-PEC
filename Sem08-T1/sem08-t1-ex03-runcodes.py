
def verificaMaiorEMenor(modo, a, b, c, d, e):
    if modo == 'M':
        if a > b and a > c and a > d and a > e:
            return a
        elif b > a and b > c and b > d and b > e:
            return b
        elif c > a and c > b and c > d and c > e:
            return c
        elif d > a and d > b and d > c and d > e:
            return d
        elif e > a and e > b and e > c and e > d:
            return e
    else:
        if a < b and a < c and a < d and a < e:
            return a
        elif b < a and b < c and b < d and b < e:
            return b
        elif c < a and c < b and c < d and c < e:
            return c
        elif d < a and d < b and d < c and d < e:
            return d
        elif e < a and e < b and e < c and e < d:
            return e

def main():
    numA = int(input())
    numB = int(input())
    numC = int(input())
    numD = int(input())
    numE = int(input())

    print(verificaMaiorEMenor('M', numA, numB, numC, numD, numE))
    print(verificaMaiorEMenor('m', numA, numB, numC, numD, numE))

if __name__ == '__main__':
    main()