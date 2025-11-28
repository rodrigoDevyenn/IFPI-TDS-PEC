def encontrarPorsicao(a, c, l):
    
    posicao = a.find(l)
    novaPosicao = (posicao + c) % 26
    return novaPosicao

def criptografar(a, p):
    return a[p]

def main():
    
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    chave = int(input('Insira a chave, isto é, o tamanho do deslocamento: '))
    letra = input('Insira a letra a ser criptografada: ').strip()

    posicao = encontrarPorsicao(alfabeto, chave, letra)
    print(f'A letra {letra} criptografada com a chave {chave} é {criptografar(alfabeto, posicao)}!')
    
if __name__ == '__main__':
    main()