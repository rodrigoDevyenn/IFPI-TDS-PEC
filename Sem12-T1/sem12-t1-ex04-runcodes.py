
def numeroDaSorte(n):
    string = str(n)
    soma = 0
    for i in range(len(string)):
        soma += int(string[i])
    return soma

def main():
    data_nasc = int(input())
    print(numeroDaSorte(data_nasc))

if __name__ == '__main__':
    main()