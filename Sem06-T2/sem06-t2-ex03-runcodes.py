
def calcula_preco(qtd, val):
    return qtd * val

def total(m, b):
    return m + b

def main():

    preco_maca = float(input())
    preco_banana = float(input())
    
    print(f"{total(calcula_preco(3, preco_maca), calcula_preco(2, preco_banana)):.2f}")

if __name__ == "__main__":
    main()