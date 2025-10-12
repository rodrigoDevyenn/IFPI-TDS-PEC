
def identificador_genero(g, n):
    if g == 1:
        return f"Ilmo Sr. {n}"
    elif g == 2:
        return f"Ilma Sra. {n}"
    else:
        return None

def main():
    
    nome = input('Nome: ').strip()
    genero = int(input("Gênero(1 - Masculino, 2 - Feminino): "))

    print(identificador_genero(genero, nome))

if __name__ == "__main__":
    main()