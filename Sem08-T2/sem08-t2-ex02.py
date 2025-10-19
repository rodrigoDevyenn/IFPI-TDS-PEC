
def verificaNumero(n):
    if n > 0 and n < 100000:
        return somaDigitos(n)
    else:
        return -1

def somaDigitos(n):
     if len(str(n)) == 5:
         u = n % 10
         d = (n // 10) % 10
         c = (n //100) % 10
         m = (n // 1000) % 10
         dm = n // 10000
         return u + d + c + m + dm

     elif len(str(n)) == 4:
        u = n % 10
        d = (n // 10) % 10
        c = (n // 100) % 10
        m = n // 1000
        return u + d + c + m
     
     elif len(str(n)) == 3:
        u = n % 10
        d = (n // 10) % 10
        c = n // 100
        return u + d + c
     
     elif len(str(n)) == 2:
        u = n % 10
        d = (n // 10) % 10
        return u + d
     
     elif len(str(n)) == 1:
         return n
        
def main():

    num = int(input('Insira um número inteiro: '))
    print(verificaNumero(num))

if __name__ == '__main__':
    main()