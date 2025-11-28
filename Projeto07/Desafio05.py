
def caracteresIguais(n1, n2):
    nomea = n1.lower().replace(' ', '')
    nomeb = n2.lower().replace(' ', '')
    pontos = 0
    for i in nomea:
        if i in nomeb:
            pontos += 2
    return pontos

def caracteresAmor(n1, n2):
    nomea = n1.lower().replace(' ', '')
    nomeb = n2.lower().replace(' ', '')
    pontos = 0
    for i in nomea:
        if i in 'amor':
            pontos += 1
    for i in nomeb:
        if i in 'amor':
            pontos += 1
    return pontos

def main():
    
    nome1 = input('Insira o nome da primeira pessoa: ').strip()
    nome2 = input('Insira o nome da segunda pessoa: ').strip()

    compatibilidade = 0
    compatibilidade += caracteresIguais(nome1, nome2)
    compatibilidade += caracteresAmor(nome1, nome2)

    if compatibilidade < 5:
        print(f'Compatibilidade: {compatibilidade}. Vocês não são compatíveis!')
    elif compatibilidade >= 5 and compatibilidade < 8:
        print(f'Compatibilidade: {compatibilidade}. Compatíveis!')
    else:
        print(f'Compatibilidade: {compatibilidade}. Feitos um para outro!')




if __name__ == '__main__':
    main()