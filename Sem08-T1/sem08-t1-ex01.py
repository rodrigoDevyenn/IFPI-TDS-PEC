def calcula_idade(d, m, a, yd, ym, ya):
     if (d >= yd) and (m >= ym):
          return a - ya
     else:
          return (a - ya) - 1

def main():
     dia = int(input('Dia: '))
     mes = int(input('Mês: '))
     ano = int(input('Ano: '))

     nasci_dia = int(input('Qual dia você nasceu? '))
     nasci_mes = int(input('Qual mês você nasceu? '))
     nasci_ano = int(input('Qual ano você nasceu? '))

     print(calcula_idade(dia, mes, ano, nasci_dia, nasci_mes, nasci_ano))

if __name__ == '__main__':
     main()