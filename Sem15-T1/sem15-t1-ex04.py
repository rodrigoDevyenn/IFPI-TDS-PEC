
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


def verifica(p, c):
    cidades = []
    for uf, ibge, nome, _, _, pop in c:
        if pop > p:
            cidades.append((ibge, nome, uf, pop))
    return cidades

def main():

    populacao = int(input('Insira a população: '))

    cidades = carrega_cidades()
    listaCidades = verifica(populacao, cidades)

    print(f'CIDADES COM MAIS DE {populacao} HABITANTES:')
    for ibge, nome, uf, pop in listaCidades:
        print(f'IBGE: {ibge} - {nome}({uf}) - POPULAÇÃO: {pop}')

if __name__ == '__main__':
    main()