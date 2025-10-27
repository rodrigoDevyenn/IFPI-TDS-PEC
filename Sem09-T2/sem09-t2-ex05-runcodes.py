
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

    pA = input().strip().upper()
    pB = input().strip().upper()
    pC = input().strip().upper()
    pD = input().strip().upper()
    pE = input().strip().upper()

    contador = verificaRespostas(pA, pB, pC, pD, pE)
    print(resultado(contador))

if __name__ == '__main__':
    main()