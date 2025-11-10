
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

def main():
    maior = menor = cont = 0
    print('Insira indefinidamente números inteiros, e finalize com 0: ')
    while True:
        num = int(input('Insira um número: '))
        if num != 0:
            cont += 1
            maior = maiorOrMenor(num, maior, 2)
            if cont == 1:
                menor  = maiorOrMenor(num, menor, 0)
            else:
                menor = maiorOrMenor(num, menor, 1)
        else:
            break
    print(f'o maior número lido foi {maior}.')
    print(f'o menor número lido foi {menor}.')

if __name__ == '__main__':
    main()