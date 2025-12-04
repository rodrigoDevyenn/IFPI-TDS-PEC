
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


def verifica(p, m, c):
    cidades = []
    for uf, _, nome, dia, mes, pop in c:
        if pop > p and mes == m:
            cidades.append((nome, uf, pop, dia, mes))
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

    mes = int(input('Insira o mês: '))
    populacao = int(input('Insira a população: '))

    cidades = carrega_cidades()
    listaCidades = verifica(populacao, mes, cidades)

    print(f'CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM {nomeMeses(mes).upper()}:')
    for nome, uf, pop, dia, mes in listaCidades:
        print(f'{nome}({uf}) tem {pop} habitantes e faz aniversário em {dia} de {nomeMeses(mes).lower()}.')

if __name__ == '__main__':
    main()