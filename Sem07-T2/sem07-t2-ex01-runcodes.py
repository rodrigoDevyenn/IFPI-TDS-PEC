
def conjuge():
    nome = input().strip().upper()
    return nome

def totalDeCaracteres(n, es):
    if es == '1':
        return len(conjuge() + n )
    elif es == '2':
        return len(n)
    else:
        return None

def main():
    
    nome = input().strip().upper()
    estado_civil = input().strip()

    print(totalDeCaracteres(nome, estado_civil))

if __name__ == '__main__':
    main()