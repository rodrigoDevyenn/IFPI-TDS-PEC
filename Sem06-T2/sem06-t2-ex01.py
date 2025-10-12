
def contagem(f):
    return len(f)

def main():
    
    frase = str(input("Insira a frase: ")).strip()

    print(contagem(frase))

if __name__ == "__main__":
    main()