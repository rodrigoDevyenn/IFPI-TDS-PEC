def quantidadeDigitos(n):
    return len(str(n))

def separaDigitos(n, casa):
    unidade = dezena = centena = 0
    if quantidadeDigitos(n) == 1:
        unidade = n
        if casa == 'u':
            return unidade
        elif casa == 'd':
            return dezena
        elif casa == 'c':
            return centena
    elif quantidadeDigitos(n) == 2:
        unidade = n % 10
        dezena = (n // 10) % 10
        if casa == 'u':
            return unidade
        elif casa == 'd':
            return dezena
        elif casa == 'c':
            return centena
    elif quantidadeDigitos(n) == 3:
        unidade = n % 10
        dezena = (n // 10) % 10
        centena = n // 100
        if casa == 'u':
            return unidade
        elif casa == 'd':
            return dezena
        elif casa == 'c':
            return centena

def numerosEmPalavras(n):
    if n == 0:
        return 'zero'
    elif n == 1:
        return 'uma'
    elif n == 2:
        return 'duas'
    elif n == 3:
        return 'três'
    elif n == 4:
        return 'quatro'
    elif n == 5:
        return 'cinco'
    elif n == 6:
        return 'seis'
    elif n == 7:
        return 'sete'
    elif n == 8:
        return 'oito'
    elif n == 9:
        return 'nove'

def porExtenso(n, casa):
    if casa == 'u':
        if separaDigitos(n, casa) == 1:
            return f'{numerosEmPalavras(separaDigitos(n, casa))} unidade'
        else:
            return f'{numerosEmPalavras(separaDigitos(n, casa))} unidades'
    elif casa == 'd':
        if separaDigitos(n, casa) == 1:
             return f'{numerosEmPalavras(separaDigitos(n, casa))} dezena'
        else:
            return f'{numerosEmPalavras(separaDigitos(n, casa))} dezenas'
    elif casa == 'c':
        if separaDigitos(n, casa) == 1:
            return f'{numerosEmPalavras(separaDigitos(n, casa))} centena'
        else:
            return f'{numerosEmPalavras(separaDigitos(n, casa))} centenas'
        
def montarString(n):
        unidade = separaDigitos(n, 'u')
        dezena = separaDigitos(n, 'd')
        centena = separaDigitos(n, 'c')
        string = ''
        if centena != 0:
            string = string + porExtenso(n, 'c')
        if dezena != 0:
            if centena != 0 and unidade != 0:
                string = string + ', ' + porExtenso(n, 'd')
            elif centena != 0:
                string = string + ' e ' + porExtenso(n, 'd')
            else:
                string = string + porExtenso(n, 'd')
        if unidade != 0:
            if centena != 0  or dezena != 0:
                string = string + ' e ' + porExtenso(n, 'u')
            else:
                string = string + porExtenso(n, 'u')
        return string + '.'
            

def main():

    num = int(input())
    print(montarString(num))

if __name__ == '__main__':
    main()