def porcentagem(x, por):
    return x * (por / 100)

def relatorioExtincao(p):
    relatorio = ""
    mortos = porcentagem(p, 6)
    nascidos = porcentagem(p, 1)
    pt = p
    ano = 1600
    while True:
        mortos = porcentagem(pt, 6)
        nascidos = porcentagem(pt, 1)
        pt = pt + (nascidos) - (mortos)
        relatorio += f'{ano:.0f},{nascidos:.0f},{mortos:.0f},{pt:.0f}'
        if pt < (porcentagem(p, 10) ):
            break
        relatorio += '\n'
        ano += 1
    return relatorio



def main():
    populacao = int(input('Insira a população inicial: '))
    print(relatorioExtincao(populacao))

if __name__ == '__main__':
    main()