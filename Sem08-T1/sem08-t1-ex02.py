
def verificaData(dA, mA, aA, dB, mB, aB):
     if aA > aB:
          return (f'{dA}/{mA}/{aA}')
     elif aA == aB and mA > mB:
          return (f'{dA}/{mA}/{aA}')
     elif aA == aB and mA == mB and dA > dB:
          return (f'{dA}/{mA}/{aA}')
     else:
          return (f'{dB}/{mB}/{aB}')

def main():
     print('Primeira data:')
     dataA_d = int(input('Dia: '))
     dataA_m = int(input('Mês: '))
     dataA_a = int(input('Ano: '))

     print('Segunda data:')
     dataB_d = int(input('Dia: '))
     dataB_m = int(input('Mês: '))
     dataB_a = int(input('Ano: '))

     print(verificaData(dataA_d, dataA_m, dataA_a, dataB_d, dataB_m, dataB_a))

if __name__ == '__main__':
     main()