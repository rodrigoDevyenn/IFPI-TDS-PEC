
def verificacao(d, m, a):
    if m < 1 or m > 12:
        return False
    if a < 1:
        return False
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if d < 1 or d > 31:
            return False
    if m == 4 or m == 6 or m == 9 or m == 11:
        if d < 1 or d > 30:
            return False
    if m == 2:
        if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):
            if d < 1 or d > 29:
                return False
        elif d < 1 or d > 28:
            return False
    return True

def main():

    data = input().strip()
    dia = int(data[0:2])
    mes = int(data[2:4])
    ano = int(data[4:8])

    print(verificacao(dia, mes, ano))

if __name__ == '__main__':
    main()