def questao01():
    print('''
          Q1 - No Python, como se chama uma "caixa" usada para armazenar dados?
          a - texto
          b - variavel
          c - uma caixa de sapatos
          ''')
    resposta = input().lower()
    if resposta == 'a':
        print('Não - texto é um tipo de dado :(')
        return 0
    elif resposta == 'b':
        print('Correto!! :)')
        return 1
    elif resposta == 'c':
        print('Não seja bobinho! :(')
        return 0
    else:
        print('Você não escolheu a, b ou c :(')
        return 0

def questao02():
    print('''
          Q2 - No Python, como se chama uma a função que receber dados do usuario?
          a - input
          b - variavel
          c - print
          ''')
    resposta = input().lower()
    if resposta == 'a':
        print('Correto!! :)')
        return 1
    elif resposta == 'b':
        print('Não, Variável é para armazenar dados :(')
        return 0
    elif resposta == 'c':
        print('Não, print é outra coisa :(')
        return 0
    else:
        print('Você não escolheu a, b ou c :(')
        return 0

def questao03():
    print('''
          Q2 - No Python, como se chama uma a função que imprime informações na tela?
          a - for
          b - elif
          c - print
          ''')
    resposta = input().lower()
    if resposta == 'a':
        print('Não, for é um comando de repetição! :(')
        return 0
    elif resposta == 'b':
        print('Não, Passou longe! :(')
        return 0
    elif resposta == 'c':
        print('Correto!! :)')
        return 1
    else:
        print('Você não escolheu a, b ou c :(')
        return 0
    

def main():
    score = 0
    score += questao01()
    score += questao02()
    score += questao03()

    print(f'O seu score foi {score}!')
    
if __name__ == '__main__':
    main()