
def conjuge():
    nome = input('Insira o nome do cônjuge: ').strip().upper()
    return nome

def totalDeCaracteres(n, es):
    if es == "1":
        return len(conjuge() + n )
    elif es == '2':
        return len(n)
    else:
        return None

def main():
    
    nome = input('Nome: ').strip().upper()
    estado_civil = input('Estado Civíl(1 - Casado, 2 - Solteiro): ').strip().upper()

    print(totalDeCaracteres(nome, estado_civil))

if __name__ == '__main__':
    main()