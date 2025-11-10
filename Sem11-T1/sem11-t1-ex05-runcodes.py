
def aumentoPercentual(v, p):
    return (v * (p/100))

def evolucao(s, d):
    mes = 10
    ano = 2016
    while True:
        if mes < 12:
            mes += 1
        else:
            mes = 1
            ano += 1
        d = d + aumentoPercentual(d, 15)
        if mes == 3:
            s = s + aumentoPercentual(s, 5)
        if d > s:
            break
    return f'{mes}/{ano}'

def main():
    
    salario = float(input())
    divida = float(input())

    print(evolucao(salario, divida))

if __name__ == '__main__':
    main()