
def verificaNumero(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FIZZBUZZ'
    elif n % 3 == 0:
        return 'FIZZ'
    elif n % 5 == 0:
        return 'BUZZ'
    else: 
        return n

def main():

    num = int(input('Insira um núemro inteiro: '))
    print(verificaNumero(num))

if __name__== '__main__':
    main()