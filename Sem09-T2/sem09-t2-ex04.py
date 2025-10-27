
def calculaPreco(kg_mo, kg_ma):
    if kg_mo <= 5:
        totalMorangos = kg_mo * 2.50
    elif kg_mo > 5:
        totalMorangos = kg_mo * 2.20
    if kg_ma <= 5:
        totalMaca = kg_ma * 1.80
    elif kg_ma > 5:
        totalMaca = kg_ma * 1.50
    return totalMorangos + totalMaca

def calculaKg(kg_mo, kg_ma):
    return kg_mo + kg_ma

def valorFinal(p, kg_mo, kg_ma):
    if calculaKg(kg_mo, kg_ma) > 8 or p > 25.00:
        return f'{p - (p * 0.10):.2f}'
    else:
        return f'{p:.2f}'

def main():

    morango = float(input('Quantidade de Morangos em Kg: '))
    maca = float(input('Quantidade de Maçãs em Kg: '))

    print(valorFinal(calculaPreco(morango, maca), morango, maca))

if __name__ == '__main__':
    main()