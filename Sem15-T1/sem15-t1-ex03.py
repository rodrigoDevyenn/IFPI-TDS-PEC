def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado


def verifica(d, m, c):
    cidades = []
    for uf, _, nome, dia, mes, _ in c:
        if dia == d and mes == m:
            cidades.append((nome, uf))
    return cidades

def nomeMeses(m):
    if m == 1:
        return 'Janeiro'
    elif m == 2:
        return 'Fevereiro'
    elif m == 3:
        return 'Março'
    elif m == 4:
        return 'Abril'
    elif m == 5:
        return 'Maio'
    elif m == 6:
        return 'Junho'
    elif m == 7:
        return 'Julho'
    elif m == 8:
        return 'Agosto'
    elif m == 9:
        return 'Setembro'
    elif m == 10:
        return 'Outubro'
    elif m == 11:
        return 'Novembro'
    elif m == 12:
        return 'Dezembro'

def main():

    dia = int(input('Insira o dia: '))
    mes = int(input('Insira o mês: '))
    
    cidades = carrega_cidades()
    listaCidades = verifica(dia, mes, cidades)

    print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {nomeMeses(mes).upper()}:')
    for cidade, uf in listaCidades:
        print(f'{cidade}({uf})')

if __name__ == '__main__':
    main()



