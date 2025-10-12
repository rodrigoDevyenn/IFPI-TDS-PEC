
def sinal_De_Transito(c):
    if c == "V":
        return "Siga"
    elif c == "A":
        return "Atenção"
    elif c == "E":
        return "Pare"
    else:
        return None

def main():

    cor = input().strip().upper()
    print(sinal_De_Transito(cor))

if __name__ == '__main__':
    main()