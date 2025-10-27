
def verificaRespostas(pa, pb, pc, pd, pe):
    c = 0
    if pa == 'S':
        c += 1
    if pb == 'S':
        c += 1
    if pc == 'S':
        c += 1
    if pd == 'S':
        c += 1
    if pe == "S":
        c += 1
    return c

def resultado(c):
    if c == 2:
        return 'Suspeito'
    elif 3 <= c <= 4:
        return 'Cúmplice'
    elif c == 5:
        return 'Assassino'
    else: 
        return 'Inocente'

def main():

    pA = input("Telefonou para a vítima ?").strip().upper()
    pB = input("Esteve no local do crime ?").strip().upper()
    pC = input("Mora perto da vítima ?").strip().upper()
    pD = input("Devia para a vítima ?").strip().upper()
    pE = input("Já trabalhou com a vítima ?").strip().upper()

    contador = verificaRespostas(pA, pB, pC, pD, pE)
    print(resultado(contador))

if __name__ == '__main__':
    main()