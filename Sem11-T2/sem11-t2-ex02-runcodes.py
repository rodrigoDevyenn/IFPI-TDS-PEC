
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
    while True:
        idade = int(input())
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
    print(cont)
    print(f'{media(soma, cont):.2f}')
    print(menor)
    print(maior)

if __name__ == '__main__':
    main()