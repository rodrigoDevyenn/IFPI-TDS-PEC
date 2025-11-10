
def maiorOrMenor(n, x, m):
    if m == 0:
          return n
    elif m == 1:
        if n < x:
            return n
        else:
            return x 
    else:
        if n > x:
            return n
        else:
            return x 

def media(s, qtd):
    return s / qtd

def main():
    soma = cont = maior = menor = 0
    print('Insira a idade de pessoas indefinidamente, finalize com 0!')
    while True:
        idade = int(input('Insira a idade: '))
        if idade != 0:
            cont += 1
            soma = soma + idade
            maior = maiorOrMenor(idade, maior, 2)
            if cont == 1:
                menor = maiorOrMenor(idade, menor, 0)
            else:
                menor = maiorOrMenor(idade, menor, 1)
        else:
            break 
    print(f'O Número de pessoas é {cont}.')
    print(f'A Idade média do grupo é {media(soma, cont):.2f}.')
    print(f'A menor idade é {menor}.')
    print(f'A maior idade é {maior}.')

if __name__ == '__main__':
    main()