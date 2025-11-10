
def calcula(val, tax):
    return val + (val  * tax/100)

def evolucao(d, t):
    ano = 0
    valor = d
    while valor < (d * 2):
        valor = calcula(valor, t)
        ano += 1
    return ano

def main():
    
    deposito = float(input())
    taxa = float(input())
    
    print(evolucao(deposito, taxa))

if __name__ == '__main__':
    main()