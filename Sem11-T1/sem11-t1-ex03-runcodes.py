
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
    while True:
        num = int(input())
        if num != 0:
            cont += 1
            maior = maiorOrMenor(num, maior, 2)
            if cont == 1:
                menor  = maiorOrMenor(num, menor, 0)
            else:
                menor = maiorOrMenor(num, menor, 1)
        else:
            break
    print(maior)
    print(menor)

if __name__ == '__main__':
    main()