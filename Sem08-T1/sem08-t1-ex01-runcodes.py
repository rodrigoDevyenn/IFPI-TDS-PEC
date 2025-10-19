def calcula_idade(d, m, a, yd, ym, ya):
     if (d >= yd) and (m >= ym):
          return a - ya
     else:
          return (a - ya) - 1

def main():
     dia = int(input())
     mes = int(input())
     ano = int(input())

     nasci_dia = int(input())
     nasci_mes = int(input())
     nasci_ano = int(input())

     print(calcula_idade(dia, mes, ano, nasci_dia, nasci_mes, nasci_ano))

if __name__ == '__main__':
     main()