
def tipo_Caractere(c):
    if c in ('A', 'E', 'I', 'O', 'U'):
        return "vogal"
    elif 'A' <= c <= 'Z' and (c not in('A', 'E', 'I', 'O', 'U')):
        return "consoante"
    elif '0' <= c <= '9':
        return "número"
    else:
        return "símbolo"

def main():

    caractere = input('Insira um caractere: ').strip().upper()
    print(tipo_Caractere(caractere))

if __name__ == '__main__':
    main()