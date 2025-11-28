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

def Alfabeto(i):
    a1 = 'abcdefghijklmnopqrstuvwxyz'
    a2 = 'twjxaprbdcsqfgleyuvnimkhzo'
    a3 = 'gfvylkxwhebptniqcdaousjzmr'
    a4 = 'lmzbrctwfgxnjdqoiyphvekasu'
    a5 = 'cwozdslvhiugxrfynakmpeqjtb'
    Lista = [a1, a2, a3, a4, a5]
    return Lista[i]

def menu():
    return '\n=====MENU=====\n1.Criptografar Uma Letra\n2.Cripografar uma Mensagem\n3.Descriptografar uma Letra\n4.Descriptografar uma Mensagem\n5.Embaralhar o Alfabeto\n6.Finalizar\n'

def main():
    
    alfabeto = 0
    while True:
        print(menu())
        op = input('Escolha uma opção: ')

        if op == '1':
            letra = input('\nInsira a letra a ser criptografada: ').strip()
            chave = int(input('Insira a chave: '))
            print(f'\nA letra {letra} criptografada com a chave {chave} é {criptografar(Alfabeto(alfabeto), chave, letra)}!')
        elif op == '2':
            mensagem = input('Insira a mensagem a ser criptografada: ').strip()
            chave = int(input('Insira a chave: '))
            print(f'\nA mensagem {mensagem} criptograda com a chave {chave} é "{criptografarMensagem(Alfabeto(alfabeto), chave, mensagem)}"!')
        elif op == '3':
            letra = input('Insira a letra a ser descriptografada: ').strip()
            chave = int(input('Insira a chave: '))
            print(f'\nA letra {letra} descriptografada com a chave {chave} é {descriptografar(Alfabeto(alfabeto), chave, letra)}!')
        elif op == '4':
            mensagem = input('Insira a mensagem a ser descriptografada: ').strip()
            chave = int(input('Insira a chave: '))
            print(f'\nA mensagem {mensagem} criptograda com a chave {chave} é "{descriptografarMensagem(Alfabeto(alfabeto), chave, mensagem)}"!')
        elif op == '5':
            alfabeto = (alfabeto + 1) % 5
            print('\nAlfabeto alterado com sucesso!')
        elif op == '6':
            print('Finalizando...')
            break
        else:
            print('\nOpção Inválida! Tente Novamente.')
    
if __name__ == '__main__':
    main()