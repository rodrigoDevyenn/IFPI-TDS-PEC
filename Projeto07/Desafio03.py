def descriptografarMensagem(a, c, m):
    mensagemOriginal = ''
    for l in m:
        if l in a:
            mensagemOriginal += descriptografar(a, c, l)
        else: 
            mensagemOriginal += l
    return mensagemOriginal

def criptografarMensagem(a, c, m):
    mensagemCriptografada = ''
    for l in m:
        if l in a:
            mensagemCriptografada += criptografar(a, c, l)
        else: 
            mensagemCriptografada += l
    return mensagemCriptografada

def criptografar(a, c, l):

    posicao = a.find(l)
    novaPosicao = (posicao + c) % 26
    return a[novaPosicao]

def descriptografar(a, c, l):
    
    posicao = a.find(l)
    posicaoOriginal = (posicao - c) % 26
    return a[posicaoOriginal]

def menu():
    return '\n=====MENU=====\n1.Criptografar Uma Letra\n2.Cripografar uma Mensagem\n3.Descriptografar uma Letra\n4.Descriptografar uma Mensagem\n5.Finalizar'

def main():
    
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        print(menu())
        op = input('Escolha uma opção: ')

        if op == '1':
            letra = input('\nInsira a letra a ser criptografada: ').strip()
            chave = int(input('Insira a chave: '))
            print(f'\nA letra {letra} criptografada com a chave {chave} é {criptografar(alfabeto, chave, letra)}!')
        elif op == '2':
            mensagem = input('Insira a mensagem a ser criptografada: ').strip()
            chave = int(input('Insira a chave: '))
            print(f'\nA mensagem {mensagem} criptograda com a chave {chave} é "{criptografarMensagem(alfabeto, chave, mensagem)}"!')
        elif op == '3':
            letra = input('Insira a letra a ser descriptografada: ').strip()
            chave = int(input('Insira a chave: '))
            print(f'\nA letra {letra} descriptografada com a chave {chave} é {descriptografar(alfabeto, chave, letra)}!')
        elif op == '4':
            mensagem = input('Insira a mensagem a ser descriptografada: ').strip()
            chave = int(input('Insira a chave: '))
            print(f'\nA mensagem {mensagem} criptograda com a chave {chave} é "{descriptografarMensagem(alfabeto, chave, mensagem)}"!')
        elif op == '5':
            print('Finalizando...')
            break
        else:
            print('\nOpção Inválida! Tente Novamente.')
            
    
if __name__ == '__main__':
    main()