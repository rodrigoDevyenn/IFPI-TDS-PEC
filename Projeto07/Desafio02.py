def descriptografarMensagem(a, c, m):
    mensagemOriginal = ''
    for i in range(len(m)):
        posicao = a.find(m[i])
        posicaoOriginal = (posicao - c) % 26
        mensagemOriginal += a[posicaoOriginal]
    return mensagemOriginal

def encontrarPorsicao(a, c, l):
    
    posicao = a.find(l)
    novaPosicao = (posicao + c) % 26
    return novaPosicao

def criptografar(a, p):
    return a[p]

def menu():
    return '=====MENU=====\n1.Criptografar Uma Letra\n2.Descripografar uma Mensagem\n3.Finalizar'

def main():
    
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        print(menu())
        op = input('Escolha uma opção: ')

        if op == '1':
            chave = int(input('Insira a chave, isto é, o tamanho do deslocamento: '))
            letra = input('Insira a letra a ser criptografada: ').strip()
            posicao = encontrarPorsicao(alfabeto, chave, letra)
            print(f'A letra {letra} criptografada com a chave {chave} é {criptografar(alfabeto, posicao)}!')
        elif op == '2':
            chave = int(input('Insira a chave, isto é, o tamanho do deslocamento: '))
            mensagem = input('Insira a mensagem a ser descriptografada: ').strip()
            print(descriptografarMensagem(alfabeto, chave, mensagem))
        else:
            break
    
if __name__ == '__main__':
    main()